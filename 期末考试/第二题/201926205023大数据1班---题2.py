import numpy as np
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
# 用于存放信息的列表
list = []
# 解析hmtl页面
def getdata():
    soup = BeautifulSoup(open('./data/page3.html', encoding='utf-8'), features='lxml')
    for each in soup.tbody.find_all('tr'):
        th = each.select('th')
        td = each.select('td')
        listli = [th[0].string, td[0].string, td[1].string, td[2].string, td[3].text, th[1].text]
        list.append(listli)
    print(list)


# 先保存在CSV里面
def save_csv():
    with open('page3.csv', 'w', newline='', encoding='utf-8-sig') as f:
        wr = csv.writer(f)
        wr.writerow(['成交时间', '成交价', '价格变动', '成交量（手）', '成交额（元）', '性质'])
        wr.writerows(list)
    f.close()

# 计算最大值、最小值
def max_min():
    listsum = []
    for i in list:
        listsum.append(float(i[1]))
    print(listsum)
    min = np.min(listsum)
    max = np.max(listsum)
    print("成交价最大值：" )
    print(max)
    print("成交价最小值：" )
    print(min)


# 总交易额，平均值
def jiaoyi():
    listsum = []
    sum = 0
    for i in list:
        listsum.append(int(i[4].replace(",","")))
    for j in listsum:
        sum += j
    print('总交易额为：')
    print(sum)
    avg = np.mean(listsum)
    print('平均值为：')
    print(avg)

# 按分钟统计交易额
def countfen():
    sum53 = 0
    sum52 = 0
    sum51 = 0
    sum50 = 0
    for i in list:
        str = i[0]
        sp = str.split(':')
        if sp[1]=='53':
            sum53+=int(i[4].replace(",",""))
        elif sp[1]=='52':
            sum52 += int(i[4].replace(",",""))
        elif sp[1]=='51':
            sum51 += int(i[4].replace(",",""))
        elif sp[1]=='50':
            sum50 += int(i[4].replace(",",""))
    print('14:53的成交额为：')
    print(sum53)
    print('14:52的成交额为：')
    print(sum52)
    print('14:51的成交额为：')
    print(sum51)
    print('14:50的成交额为：')
    print(sum50)
    # 用Matplotlib显示分钟交易额
    x = ['50', '51', '52', '53']
    # y = [sum50, sum51, sum52, sum53]
    y = []
    y.append(sum50)
    y.append(sum51)
    y.append(sum52)
    y.append(sum53)
    print(y)
    plt.plot(x,y,"g",marker='D',markersize=5, label="分钟交易额")
    #绘制坐标轴标签
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.xlabel("分钟")
    plt.ylabel("交易额")
    plt.title("分钟交易额")
    plt.show()

if __name__ == '__main__':
    getdata()
    save_csv()
    max_min()
    jiaoyi()
    countfen()
