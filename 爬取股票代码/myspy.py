import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 入口函数
if __name__ == '__main__':
    daima = input('请输入股票代码：')
    datetime = input('请输入时间(xxxx-xx-xx):')
    page = 1  # 从第一页开始抓
    list = []

    while True:
        time.sleep(2)
        print(page)
        url = r'http://market.finance.sina.com.cn/transHis.php?symbol=' + daima + '&date=' + datetime + '&page=' + str(
            page)
        # 进行伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }
        # 发送请求
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        htmlcontent = response.text
        print("状态码：" + str(response.status_code))
        # 寻找并解析
        soup = BeautifulSoup(htmlcontent, 'lxml').findAll('tr')
        if len(soup) == 1:
            break;
        for i in range(1, len(soup)):
            ls = []
            ls.append(soup[i].findAll('td')[0].text)
            ls.append(eval(soup[i].findAll('td')[0].text))
            ls.append(soup[i].findAll('td')[1].text)
            ls.append(soup[i].findAll('td')[2].text)
            ls.append(soup[i].findAll('td')[3].text)
            ls.append(soup[i].findAll('th')[1].text)
            list.append(ls)
        page += 1
        break
    tp = pd.DataFrame(list, columns=['成交时间', '成交价', '价格变动', '成交量(手)', '成交额(元)', '性质'])
    if os.path.exists('./data/' + daima + '-' + datetime + '.csv'):
        os.remove('./data/' + daima + '-' + datetime + '.csv')
    tp.to_csv(r'./data/' + daima + '-' + datetime + '.csv', encoding='utf_8_sig')
    print('max:' + str(tp.iloc[:, 1].max()))
    print('min:' + str(tp.iloc[:, 1].min()))
    print('mean:' + str(tp.iloc[:, 1].mean()))
