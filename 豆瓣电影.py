import requests, json

url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
data = {
    'sort': 'U',
    'range': '0,10',
    'tags': '',
    'start': '0'
}

response = requests.get(url=url, params=data, headers=ua)
r = response.json()

with open('豆瓣电影详细.json', 'w', encoding='utf8') as f:
    json.dump(r, f)
