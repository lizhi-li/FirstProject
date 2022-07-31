import requests
if __name__ == "__main__":
    # UA伪装，user-agent 请求载体的身份标识
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    }
    # 1 指定url
    # url = 'https://www.sogou.com/web?query=波晓张'
    # 处理url携带的参数
    url = 'https://www.sogou.com/web?'
    kw = input('enter a word:')
    param = {
        'query' : kw
    }
#     2 发起请求,请求过程中处理了数据
    response  = requests.get(url = url,params=param,headers=headers)
#     3 获取响应数据
    page_text = response.text
#     4 持久化存储
    filename = kw +'.xml'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功')
