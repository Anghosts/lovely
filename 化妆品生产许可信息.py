import time

import requests, json

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
print('爬取中...')
num = []
for idd in range(1, 5):
    data = {
        'on': 'true',
        'page': idd,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': ''
    }
    for i in range(15):
        time.sleep(1)
        response = requests.post(url=url, data=data, headers=ua).json()
        n = response['list'][i]
        print(n)
        num.append(n['ID'])


all_data = []
new_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for ids in num:
    new_data = {
        'id': ids
    }
    time.sleep(1)
    new_response = requests.post(url=new_url, data=new_data, headers=ua).json()
    all_data.append(new_response)
    print(new_response)

with open('化妆品生产许可信息.json', 'w', encoding='utf8') as f:
    json.dump(all_data, f, ensure_ascii=False)
print('爬取完毕!')
