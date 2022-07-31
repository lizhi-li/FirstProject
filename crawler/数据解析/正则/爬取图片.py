import requests

if __name__ == "__main__":
    url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.hookbase.com%2Fimg2017%2F3%2F30%2F201733021423378379.jpg&refer=http%3A%2F%2Fimg.hookbase.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1660786660&t=20c9de561e7269da5d4c51cf66caa006'
    img_data = requests.get(url = url).content
    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)