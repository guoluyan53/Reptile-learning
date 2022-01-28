#这是朋友的代码
import requests
import time
from bs4 import BeautifulSoup
import csv

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}
listone = []  #用于存放信息的列表

def get_message(text,page):
    soup = BeautifulSoup(text,'lxml')
    if soup.tbody.string !=None:
        return 0
    else:
        for each in soup.tbody.find_all('tr'):
            th = each.select('th')
            td = each.select('td')
            listtwo = [th[0].string,td[0].string,td[1].string,td[2].string,td[3].string,th.content[0].string]
            listone.append(listtwo)

def gethtml(gupiao,date,page):
    url = 'https://market.finance.sina.com.cn/transHis.php?symbol=' + gupiao + '&date=' + date + '&page=' + str(page)
    print(url)
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        flag = get_message(r.text, page)
        if flag == 0:
            return 0
    except Exception as result:
        print("错误原因：", result)
        return 0

def save_csv(list,gupiao,date):
    print("list",list)
    with open('sina'+gupiao+date+'.csv', 'w',newline='', encoding='utf-8-sig') as f:
        wr = csv.writer(f)
        wr.writerow(['成交时间','成交价','价格变动','成交量(手)','成交额(元)','性质'])
        wr.writerows(listone)
    f.close()

def compute(gupiao,date):
    with open('sina'+gupiao+date+'.csv','r',encoding='utf-8-sig') as f2:
        r = csv.reader(f2)
        head = next(r)
        sum = 0
        max = 0
        min=100
        count = 0
        for row in r:
            # print(row)
            thisnum = float(row[1])
            sum = sum + thisnum
            if max<thisnum:
                max = thisnum
            if min> thisnum :
                min = thisnum
            count= count+1
        avg = sum/count
        print("最大值为",max)
        print("最小值为",min)
        print("平均值为",avg)
    f2.close()

def main():
    gupiao = input("请输入你想要查询的股票（例如sz000001）：")
    date = input("请输入你想要查询的日期（格式为2021-04-27）：")
    for i in range(1,100):
        # 返回如果是0则说明爬取错误或者到达尾页，要跳出循环
        flag = gethtml(gupiao,date,i)
        # 最好需要间隔5s，否则太快爬取会被新浪封ip
        time.sleep(5)
        if flag==0:
            break
    print(listone)
    save_csv(listone,gupiao,date)
    #计算股票单价平均值最大值最小值
    compute(gupiao,date)
main()

