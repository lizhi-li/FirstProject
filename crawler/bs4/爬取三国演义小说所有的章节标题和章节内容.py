import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 对首页的页面数据进行爬取，要获取章节标签和href
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
        'cookie':'Hm_lvt_649f268280b553df1f778477ee743752=1658488286; Hm_lpvt_649f268280b553df1f778477ee743752=1658488530',
        'referer':'https://www.shicimingju.com/book/sanguoyanyi.html'
    }
    page_text = requests.get(url = url,headers=header).content.decode('utf-8','ignore')
    # print(page_text)

    # 1 实例化一个BS对象 ，将页面源码数据加载到该对象
    soup = BeautifulSoup(page_text,'lxml')
    # 解析两样
    li_list=soup.select('.book-mulu > ul > li')


    fp = open('./sanguo.txt','w',encoding='UTF-8')
    for li in li_list:
        title = li.a.string
        detail_url ='https://www.shicimingju.com'+ li.a['href']
        # 对详情页发起请求，解析内容
        detail_page_text = requests.get(url = detail_url,headers=header).content.decode('utf-8','ignore')
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text

        fp.write(title+':'+content+'\n')
        print(title+'爬取成功')