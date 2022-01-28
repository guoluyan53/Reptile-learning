# coding: utf-8
from parsel import Selector

import requests


def get(url):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
    }
    body = requests.get(url, headers=headers).content
    # 我擦, 居然出现乱码;
    xbody = Selector(text=str(body, encoding='utf-8'))
    lists = xbody.xpath("//d")
    count = xbody.xpath("//maxlimit/text()").extract_first()
    print("共有%s条弹幕" % count)
    for li in lists:
        content = li.xpath("./text()").extract_first()
        par = li.xpath("./@p").extract_first()
        print(content, ":::::", par)


if __name__ == '__main__':
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid=404210194"
    get(url)