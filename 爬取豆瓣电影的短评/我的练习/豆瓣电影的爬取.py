import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {      #url地址的参数，存放在一个对象里
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '20',  #从库中的第几个电影去取
        'limit': '20'   #一次取多少个数
    }
    #伪装UA
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari / 537.36'
    }
    #发请求
    response = requests.get(url=url,params=param,headers=headers)
    list_data = response.json()

    fp = open('douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)        

    print('结束！')
