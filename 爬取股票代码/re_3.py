import os.path
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
if __name__ == '__main__':
    sym = input('请输入股票代码:')#sz000001
    tm = input('请输入时间格式(xxxx-xx-xx):')#2021-04-27
    page = 1
    ls = []
    while True:
        time.sleep(2)
        print(page)
        post_url = r'http://market.finance.sina.com.cn/transHis.php?symbol='+sym+'&date='+tm+'&page='+str(page)+'&qq-pf-to=pcqq.c2c'
        # 进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        # 请求发送
        response = requests.get(url=post_url, headers=headers)
        response.encoding = response.apparent_encoding
        tmp = response.text
        print("状态码:"+str(response.status_code))
        # print(response.text)
        soup = BeautifulSoup(tmp, 'lxml').findAll('tr')
        if len(soup) == 1:
            break
        for i in range(1, len(soup)):
            l = []
            l.append(soup[i].findAll('th')[0].text)
            l.append(eval(soup[i].findAll('td')[0].text))
            l.append(soup[i].findAll('td')[1].text)
            l.append(soup[i].findAll('td')[2].text)
            l.append(soup[i].findAll('td')[3].text)
            l.append(soup[i].findAll('th')[1].text)
            ls.append(l)
        page += 1
    tp = pd.DataFrame(ls, columns=['成交时间', '成交价', '价格变动', '成交量(手)', '成交额(元)', '性质'])
    if os.path.exists('./data/'+sym+'-'+tm+'.csv'):
        os.remove('./data/'+sym+'-'+tm+'.csv')
    tp.to_csv(r'./data/'+sym+'-'+tm+'.csv', encoding='utf_8_sig')
    print('max:'+str(tp.iloc[:, 1].max()))
    print('min:'+str(tp.iloc[:, 1].min()))
    print('mean:'+str(tp.iloc[:, 1].mean()))
