import requests

url = 'https://www.baidu.com/s?'
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

s = input('搜索的内容：')
params = {'wd': s}

r = requests.get(url=url, params=params, headers=ua)
html = r.text
print(html)
