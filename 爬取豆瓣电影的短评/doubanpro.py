import urllib.request
from bs4 import BeautifulSoup
import time



absolute = "https://movie.douban.com/subject/26588308/comments"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}
comment_list = []


#解析html
def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    if soup.string != None:
        return 0
    else:
        for each in soup.find_all(name="span",attrs={"class": "short"}):
            textword = each.text
            comment_list.append(textword)

#获取HTML
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

#将数据写入文件
def save_txt(data):
    with open("comments2.txt","w",newline='',encoding="utf-8") as f:
        j = 1
        for i in data:
            f.write('('+ str(j) + ')' +i)
            f.write("\n")
            j+=1


if __name__ == '__main__':
    i = 0
    for j in range(0,10000000):
        flag = get_html(absolute,i)
        time.sleep(2)
        i += 20
        if flag==0:
            break
    save_txt(comment_list)

