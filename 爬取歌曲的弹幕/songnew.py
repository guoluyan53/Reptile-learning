import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
list = []

#根据url获取cid
def get_cid(url):
    data = requests.get(url=url,headers=headers)
    data = data.json()
    cid = data['data'][0]['cid']
    return cid

#获取页面
def get_html(url,cid):
    html_data = requests.get(url=url,headers=headers)
    html_data.encoding = html_data.apparent_encoding
    soup = BeautifulSoup(html_data.text,'lxml')
    data = soup.find_all('d')
    for each in data:
        print(each)
        stringword = each.text
        list.append(stringword)
    return list

#保存数据
def save_to_file(data):
    with open("dan_mu.txt", mode="w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")

def main():
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1Xf4y1A75e&jsonp=jsonp'
    # 根据url获取cid
    cid = get_cid(url)
    # 根据cid获取弹幕html
    oid_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid='+str(cid)
    data = get_html(oid_url,cid)
    # 保存弹幕
    save_to_file(data)

main()



