import requests
from lxml import etree
import os
if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kmeinv/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }
    page_text = requests.get(url =url,headers=header).text
    tree = etree.HTML(page_text)
    li_list =tree.xpath('//*[@id="main"]/div[3]/ul/li')
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]   # 网址多写了一点，出错
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        # 通用处理中文乱码的方法
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # 请求图片，持久化存储
        img_data = requests.get(url=img_src,headers=header).content
        img_path ='picLibs/'+img_name
        # print(img_name,img_src)
        with open(img_path,'wb')as fp:
            fp.write(img_data)
            print(img_name+'保存完成')