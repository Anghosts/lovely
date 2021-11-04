from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
import requests
import os
import re

# 设置无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'https://www.sevengames.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
img_list = []
count = 0

print('爬取中...')
bro = webdriver.Chrome(options=chrome_options)
# 打开网页
bro.get(url)
# 获取源码
html = bro.page_source
# 解析
pages = etree.HTML(html)
# 获取图片的地址
img_url = pages.xpath('//*[@id="all"]/div[2]/div[3]/div[3]/div/div[3]/div[3]/div[1]/div/div/div/a[1]/@href')
for http in img_url:
    if http.split('=')[-1] != 'undefined':
        img_list.append('https://www.sevengames.cn/{}'.format(http))
# for i in img_list:
#     print(i)
bro.quit()

# 打开无头浏览器
bro2 = webdriver.Chrome(options=chrome_options)
for id_url in img_list:
    bro2.get(id_url)
    # 解析原代码
    html = bro2.page_source
    img_html = etree.HTML(html)

    # 获取图片源地址
    img_path = img_html.xpath('//*[@id="imgs"]/div[@class="opus-item"]/img/@src')
    if not img_path:
        print(id_url)
        continue
    else:
        img_path = img_path[0]

    # 获取标题
    title = img_html.xpath('//*[@id="opus__exhibition"]/div/div[1]/div[1]/div[@class="title"]/text()')
    if not title:
        title = '无题'
    else:
        title = re.sub(' ', '', title[0])
        if title.split('?'):
            title = title.split('?')[0]
        if title.find('/') != -1:
            title = re.sub('/', '', title)
        if title.find("'") != -1:
            title = re.sub("'", '', title)

    # 发送请求下载图片
    img_data = requests.get(img_path, headers=headers).content
    if not os.path.exists('高清壁纸'):
        os.mkdir('高清壁纸')
    try:
        file = open('高清壁纸/' + title + '.jpg', 'wb')
        file.write(img_data)
    except OSError as oe:
        print(oe)
    print(img_path)
    count += 1

# 关闭浏览器
bro2.quit()

print('爬取完毕，共爬取{}张'.format(count))
