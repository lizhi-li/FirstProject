import json

import requests
# post请求（携带了参数）
# 响应数据是一组json数据
if __name__ == "__main__":
    # 进行UA伪装
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 1 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # post请求参数处理，（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw' :word
    }

    # 2 发送请求
    response = requests.post(url = post_url,data=data,headers=header)
#    3 获取响应数据,json方法返回的是obj，（如果确认响应数据是json类型，才可使用）
    dic_obj = response.json()
    # print(dic_obj)
#     4 持久化储存
    fileName = word +'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp = fp,ensure_ascii=False)
    # 中文不能用ASCLL码，so为False
    print('over')
