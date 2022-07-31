from bs4 import BeautifulSoup
if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    # BeautifulSoup对象使用lxml解析器进行数据解析
    # 参数一文件描述符
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup)
    # 标签名称tagName,返回的是html中第一次出现的tagName对应的标签
    # print(soup.a)
    # print(soup.div)


# soup.find('div') 等同于soup.div
#     还可属性定位
#     class加下划线_
#     print(soup.find('div',class_ ="song")) 返回一个标签
# print(soup.find_all('a')) #返回所有，，列表


# 参数放置某种选择器
# print(soup.select('.tang'))# 返回的是一个列表
#     print(soup.select('.tang > ul >li > a')[0])# 一个层级选择器
    print(soup.select('.tang > ul a')[0].text)# 空格表示多个层级
# 获取标签之间的文本内容
# soup.a.text/string/get_text()
# text和get_text:可以获取某一个标签中所有的文本内容，就算不是直系的也可以
# string：只可以获取该标签下面直系的文本内容


# 获取属性值
    print(soup.select('.tang > ul a')[0]['href'])
