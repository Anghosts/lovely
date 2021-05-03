import json

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
data = {
    'cname': '',
    'pid': '',
    'keyword': '长沙',
    'pageIndex': '1',
    'pageSize': '10'
}

response = requests.post(url=url, data=data, headers=ua)

r = response.json()
with open('肯德基餐厅查询.json', 'w', encoding='utf8') as f:
    json.dump(r, f)
