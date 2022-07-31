import requests
from lxml import etree
def demo():
    url ='https://bj.58.com/ershoufang/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }
    page_text = requests.get(url =url,headers=header).text
#     数据解析
    tree = etree.HTML(page_text)
    # title_list = tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]//h3/text()')
    # for title in title_list:
    #     print(title)
    a = tree.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[2]/a/div[2]/div[1]/div[1]/h3/text()')
    print(a+'泡泡')
    if __name__ == 'main':
        demo()
