import requests
from lxml import etree
import base64
import json
from CodeClass2 import YdmVerify
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



url = 'http://jwxtxs.tust.edu.cn:46110/login'
header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
page_text = requests.get(url =url,headers=header).text
tree = etree.HTML(page_text)
code_img_src = ''.join(tree.xpath('//*[@id="captchaImg"]/@src'))
# print(
#     code_img_src
# )
code_img_src2 = 'http://jwxtxs.tust.edu.cn:46110'+code_img_src
code_img_data = requests.get(url =code_img_src2,headers=header).content
with open('./code.jpg','wb') as fp:
    fp.write(code_img_data)


if __name__ == '__main__':
    Y = YdmVerify()
    with open('./code.jpg', 'rb') as f:
        img_content = f.read()

    print('识别结果为：', Y.common_verify(img_content))

