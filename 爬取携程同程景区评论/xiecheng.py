import requests
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
}
posturl = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList"
posturll = "https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031028411306444964"

# data_start = {
#     "arg": {
#         "channelType": "2",
#         "collapseType": "0",
#         "commentTagId": "0",
#         "pageIndex": "1",
#         "pageSize":" 10",
#         "poiId": "10558614",
#         "sortType": "3",
#         "sourceType": "1",
#         "starType": "0",
#     },
#     "head": {
#         "auth": "",
#         "cid": "09031028411306444964",
#         "ctok": "",
#         "cver": "1.0",
#         "extension": "[]",
#         "lang": "01",
#         "sid": "8888",
#         "syscode": "09",
#         "xsid": ""
#     }
# }


def gethtml():
    j = 1
    for i in range(1, 51):
        request = {
            'arg': {'channelType': '2',
                    'collapseType': '0',
                    'commentTagId': '0',
                    'pageIndex': str(i),
                    'pageSize': '10',
                    'poiId': '10558614',
                    'sortType': '3',
                    'sourceType': '1',
                    'starType': '0'},

            'head': {'auth': "",
                     'cid': "09031028411306444964",
                     'ctok': "",
                     'cver': "1.0",
                     'extension': [],
                     'lang': "01",
                     'sid': "8888",
                     'syscode': "09",
                     'xsid': ""}
        }

        time.sleep(3)
        html = requests.post(posturll, data=json.dumps(request), headers=headers)
        html1 = json.loads(html.text)
        print('正在爬取第'+str(i)+'页')
        items = html1['result']['items']
        with open("xiecheng.txt", "a", newline='', encoding='utf-8') as f:
            for k in items:
                f.write('(' + str(j) + ')' + k['content'])
                f.write("\n")
                j += 1

if __name__ == '__main__':
    gethtml()


