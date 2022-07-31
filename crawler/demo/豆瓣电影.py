import json

import requests
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        # 从库中的第几部取
        'start': '1',
        # 一次取20个
        'limit': '20'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response= requests.get(url=url,params=param,headers=header)
    list_data = response.json()
    # 列表写成json
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over')
