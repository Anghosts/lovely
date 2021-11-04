import os
import time
import requests
import threading
from lxml import etree
from multiprocessing.dummy import Pool

ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
name_list = []
index = 0


# 获取一页的ppt模板链接和模板名
def get_html(urls):
    scr_list = []

    page_text = requests.get(urls, headers=ua).text
    html = page_text.encode('iso-8859-1').decode('utf-8')
    pages = etree.HTML(html)

    src = pages.xpath('//div[@class="bot-div"]/a/@href')  # 模板原地址链接
    name = pages.xpath('//div[@class="bot-div"]/a/text()')  # 模板名

    for path in src:
        path = 'https://sc.chinaz.com' + path
        scr_list.append(path)

    for names in name:
        name_list.append(names)

    return scr_list


# 获取一个ppt模板的下载地址
def get_download_path(path):
    time.sleep(1)
    download_text = requests.get(path['url'], headers=ua).text
    html = download_text.encode('iso-8859-1').decode('utf-8')
    tree = etree.HTML(html)

    src = tree.xpath('//div[@class="download-url"]/a[1]/@href')[0]
    print()
    print('下载中...' + src, end='')
    return download_ppt(src)


# 向获取的ppt下载地址发送请求，得到ppt的二进制数据
def download_ppt(download_url):
    time.sleep(1)
    ppt_data = requests.get(download_url, headers=ua).content
    save_file('ppt免费模板7', ppt_data)


# 保存数据
def save_file(file_name, data):
    global index
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    file_path = file_name + '/' + name_list[index] + '.rar'
    with open(file_path, 'wb') as f:
        f.write(data)
    print('...OK')
    index += 1


ppt_dic = {}
urls = []


def main():
    global ppt_dic
    url = 'https://sc.chinaz.com/ppt/free_{}.html'
    for page in range(14, 15):
        for src in get_html(url.format(page)):
            ppt_dic = {'url': src}
            urls.append(ppt_dic)


if __name__ == '__main__':
    main()
    pool = Pool(4)
    pool.map(get_download_path, urls)

    pool.close()
    pool.join()
    print('全部下载完毕！')
