import json

import requests

post_url = 'https://fanyi.baidu.com/sug'
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
word = input('您要翻译的数据: ')
data = {'kw': word}

response = requests.post(url=post_url, data=data, headers=ua)

j = response.json()
with open(word + '.json', 'w', encoding='utf8') as f:
    json.dump(j, f)
    print(j)
