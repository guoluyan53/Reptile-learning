from urllib.parse import urlencode
import requests
original_url='http://sousuo.gov.cn/s.htm?t=zhengce&q='
requests_headers={
    'Referer':'http://sousuo.gov.cn/s.htm?t=zhengce&q=%E7%87%95',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

def get_one(cityid):
    p={
        'cityid':cityid
    }
    complete_url=original_url + urlencode(p)
    try:
        response=requests.get(url=complete_url,params=requests_headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse(json):
    if json:
        item=json[0].get('Name')
        print(item)

def parse_two(json):
    if json:
        for i in json:
            for b in i.get('SeriesList'):
                item_list=b.get('Name')
                print(item_list)

if __name__=='__main__':
    jo=get_one('%E7%87%95')
    parse(jo)
    print('########################')
    parse_two(jo)