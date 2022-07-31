import requests
from lxml import etree
from CodeClass import YdmVerify
import json
import base64

#封装识别验证码图片的函数
def common_verify(self, image_content, verify_type="10101"):
    # 英文数字,中文汉字,纯英文,纯数字,任意特殊字符
    # 请保证购买相应服务后请求对应 verify_type
    # verify_type="10101" 单次积分
    print(base64.b64encode(image_content).decode())
    payload = {
        "image": base64.b64encode(image_content).decode(),
        "token": '5Yi8jIh6ELVMLiRRWAnxPw==',
        "type": verify_type
    }
    resp = requests.post(self._nom_url, headers=self._headers, data=json.dumps(payload))
    print(resp.text)
    return resp.json()['data']['data']


#将验证码图片下载到本地
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = requests.get(url=url,headers=headers).text
#解析验证码图片img中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
#将验证码图片保存到了本地
with open('./code.jpg','wb') as fp:
    fp.write(img_data)


#调用打码平台的示例程序进行验证码图片数据识别
# code_text = common_verify('code.jpg',1004)
#
# print('识别结果为：',code_text)



if __name__ == '__main__':
    Y = YdmVerify()
    with open('./code.jpg', 'rb') as f:
        img_content = f.read()

    print('识别结果为：', Y.common_verify(img_content))


