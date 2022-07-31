import requests_html
from requests_html import HTMLSession
def demo():
#     实例化
    session = HTMLSession()
    # url = 'https://www.kugou.com/yy/html/rank.html'
    url = 'https://bj.58.com/ershoufang/'

    resp = session.get(url)
     # print(resp.text)

    # title_list = resp.html.xpath('//*[@id="rankWrap"]/div[2]/ul/li/a/@title')
    a = resp.html.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/text()')
    # for title in title_list:
    #     print(title)
    print(a)

if __name__=='__main__':
    demo()
