import requests
from lxml import etree
if __name__=='__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    page_text =requests.get(url =url,headers=headers).text
    tree = etree.HTML(page_text)
    hot_title =tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[1]/text()')
    hot_list=tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
    all_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]//li')

    fp2 = open('./全部城市.html','w',encoding='utf-8')
    for sin in all_list:
        sin_name = sin.xpath('./a/text()')
        sin_name2=''.join(sin_name)
        fp2.write(sin_name2+' ')

    fp=open('./全部热门城市.html','w',encoding ='utf-8')

    for hot in hot_list:
        hot_name=hot.xpath('./a/text()')
        hot_name2 = ''.join(hot_name)
        fp.write(hot_name2+' ')
    print('热门城市完成')