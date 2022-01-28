import requests
import urllib.request
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

def getdate():
    j = 1
    for i in range(1,51):
        time.sleep(2)
        geturl = "https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=8078&page=" + str(i) + "&pageSize=10"
        request = requests.get(url=geturl, headers=headers)
        html = json.loads(request.text)
        print('正在爬取第' + str(i) + '页')
        # 解析数据
        datas = html['dpList']
        with open("tongcheng.txt", "a", newline='', encoding='utf-8') as f:
            for k in datas:
                f.write('(' + str(j) + ')' + k['dpContent'])
                f.write("\n")
                j += 1




if __name__ == '__main__':
    getdate()