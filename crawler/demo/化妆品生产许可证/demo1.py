import requests

if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',


    }
    data = {
        # 'on':'true',
        # 'page':'1',
        # 'productName':'',
        # 'conditionType':'1',
        # 'applyname':'',
        # 'applysn':''
        'on':'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_ids=requests.post(url = url,headers=header,data=data).text
    print(json_ids)
    # id_list =[]
    # for dic in json_ids['list']:
    #     id_list.append(dic['ID'])
    # print(id_list)
