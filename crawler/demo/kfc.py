import requests
if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # 复制要全  url
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        # 'Cookie':'route-cell=ksa; ASP.NET_SessionId=fu1bznzd3kunguda0lc5at2u; Hm_lvt_1039f1218e57655b6677f30913227148=1658110427; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1658110427; Hm_lpvt_1039f1218e57655b6677f30913227148=1658132867; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1658132867; SERVERID=0ddc66c70f4d15b1dccd38e283ace44e|1658132945|1658132847',
        # 'Referer':'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
    }
    word = input('enter a word:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url,data=data,headers=header)
    page_text = response.text
    print(page_text)
    fileName = word +'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')
    # fp = open('./handan.html','w',encoding='utf-8')
    # json.dump(page_text,fp=fp,ensure_ascii=False)
    #
    # print('over')