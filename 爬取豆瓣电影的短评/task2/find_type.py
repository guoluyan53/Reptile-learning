#找出10页里的好评，一般或差评
import urllib.request
from bs4 import BeautifulSoup
import time


absolute = "https://movie.douban.com/subject/26588308/comments"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}
comment_list_h = []
comment_list_m = []
comment_list_l = []


#解析html
def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    if soup.string != None:
        return 0
    else:
        div = soup.findAll(name="div",attrs={"class": "comment-item"})  #这里使用find_all不行
        for each in div:
            if each.find("span",attrs={"class":"allstar50"}) or each.find("span",attrs={"class":"allstar40"}):
                textword_h = each.find("span",attrs={"class":"short"}).text
                comment_list_h.append(textword_h)
            if each.find("span",attrs={"class":"allstar30"}):
                textword_m = each.find("span", attrs={"class": "short"}).text
                comment_list_m.append(textword_m)
            if each.find("span",attrs={"class":"allstar20"}) or each.find("span",attrs={"class":"allstar10"}):
                textword_l = each.find("span", attrs={"class": "short"}).text
                comment_list_l.append(textword_l)

#获取HTML
def get_html(absolute,i):
    url = absolute + '?start=' + str(i) + '&limit=20&status=P&sort=new_score'
    print(url)
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode("UTF-8")
    flag = get_data(html)
    if flag == 0:
        return 0
    # try:

    # except Exception as result:
    #     print("错误原因",result)
    #     return 0

#将数据写入文件
def save_txt(h,m,l):
    with open("comment_type.txt","w",newline='',encoding="utf-8") as f:
        j = 1
        f.write('好评：')
        f.write("\n")
        for i in h:
            f.write('('+ str(j) + ')' +i)
            f.write("\n")
            j+=1
        f.write('一般：')
        f.write("\n")
        k = 1
        for i in m:
            f.write('(' + str(k) + ')' + i)
            f.write("\n")
            k += 1
        f.write('差评：')
        f.write("\n")
        p = 1
        for i in l:
            f.write('(' + str(p) + ')' + i)
            f.write("\n")
            p += 1
    # with open("comment_type_m.txt","w",newline='',encoding="utf-8") as f:
    #     j = 1
    #     for i in m:
    #         f.write('('+ str(j) + ')' +i)
    #         f.write("\n")
    #         j+=1
    # with open("comment_type_l.txt","w",newline='',encoding="utf-8") as f:
    #     j = 1
    #     for i in l:
    #         f.write('('+ str(j) + ')' +i)
    #         f.write("\n")
    #         j+=1


if __name__ == '__main__':
    i = 0
    for j in range(0,10):
        flag = get_html(absolute,i)
        time.sleep(2)
        i += 20
        if flag==0:
            break
    save_txt(comment_list_h,comment_list_m,comment_list_l)

