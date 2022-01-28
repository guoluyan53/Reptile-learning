import urllib.request
from bs4 import BeautifulSoup
import time
import random

#https://movie.douban.com/subject/26588308/comments?percent_type=l&limit=20&status=P&sort=new_score
#percent_type=h好评  m一般  l差评
#https://movie.douban.com/subject/26588308/comments?percent_type=l&limit=20&status=P&sort=new_score

i = 0
comment_list = []
next_page = " "
page = 0
absolute = "https://movie.douban.com/subject/26588308/comments"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # 补齐找comment_list, next_page 的代码
    while soup.string == None:
        for each in soup.find_all(name="span", attrs={"class": "short"}):
            textword = each.text
            comment_list.append(textword)


def get_html(url,page,type):
    urlget = url + '?percent_type=' + str(type) + '&start='+str(page) + '&limit=20&status=P&sort=new_score'
    print(urlget)
    request = urllib.request.Request(url=urlget, headers=headers)
    html = urllib.request.urlopen(request).read().decode("UTF-8")
    get_data(html)

def save_data(data):
    with open(u"comments.txt", 'a+', encoding='utf-8') as f:
        for l in data:
            comment = l.get_text().strip().replace("\n", "")
            f.writelines(comment + u'\n')

if __name__ == '__main__':
    lei = 'h'
    get_html(absolute,page,lei)
    save_data(comment_list)
# headers = {
#     'Host': 'movie.douban.com',
#     'Connection': ' keep-alive',
#     'Upgrade-Insecure-Requests': ' 1',
#     'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/63.0.3239.84 Safari/537.36',
#     'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Referer': 'https://www.douban.com/',
#     'Accept-Language': ' zh-CN,zh;q=0.9',
#     'Cookie': 'll="108258"; bid=fm9kQJpAfJU; _vwo_uuid_v2=DF5A8B09599CAC5A2FF17C47401F37B43|', }

# while next_page != None:
#     print(absolute + next_page)
#     request = urllib.request.Request(url=absolute + next_page, headers=headers)
#     html = urllib.request.urlopen(request).read().decode("UTF-8")
#     comment_list, next_page, i = get_data(html, i)
#
#     with open(u"comments.txt", 'a+', encoding='utf-8') as f:
#         for l in comment_list:
#             comment = l.get_text().strip().replace("\n", "")
#             f.writelines(comment + u'\n')
#     time.sleep(1 + float(random.randint(1, 50)) / 20)