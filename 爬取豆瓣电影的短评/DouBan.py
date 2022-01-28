import urllib.request
import requests
from bs4 import BeautifulSoup
import time
import random


def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    if soup.string != None:
        return 0
    else:
        for each in soup.find_all(name="span",attrs={"class": "short"}):
            textword = each.text
            comment_list.append(textword)


def get_html(url,i):
    url = absolute + '?start=' + str(i) + '&limit=20&status=P&sort=new_score'
    print(url)
    try:
        # r = requests.get(url=url, headers=headers)
        #         # r.raise_for_status()
        #         # r.encoding = r.apparent_encoding
        # flag = get_data(r.text)
        request = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(request).read().decode("UTF-8")
        flag = get_data(html)
        if flag == 0:
            return 0
    except Exception as result:
        print("错误原因",result)
        return 0

def save_txt(data):
    with open("comments.txt","w",newline='',encoding="utf-8") as f:
        j = 1
        for i in data:
            f.write('('+ str(j) + ')' +i)
            f.write("\n")
            j+=1


absolute = "https://movie.douban.com/subject/26588308/comments"
headers = {
    # 'Host':'movie.douban.com',
    # 'Connection':'keep-alive',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Referer':'https://www.douban.com/',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cookie':'ll="108258"; bid=fm9kQJpAfJU; _vwo_uuid_v2=DF5A8B09599CAC5A2FF17C47401F37B43|', }
}
comment_list = []
# next_page = " "
# while next_page != None:
#     print(absolute + next_page)
#     request = urllib.request.Request(url=absolute + next_page, headers=headers)
#     html = urllib.request.urlopen(request).read().decode("UTF-8")
#     i += 20
#     next_page = "?start=i&limit=20&status=P&sort=new_score"
def main():
    i = 0
    for j in range(0,10000000):
        flag = get_html(absolute,i)
        time.sleep(2)
        i += 20
        if flag==0:
            break
    save_txt(comment_list)

main()