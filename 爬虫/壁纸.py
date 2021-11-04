import time
import requests
import os

from lxml import etree

url = 'https://pic.netbian.com/4kdongman/index_{}.html'
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

name_list = []
index = 0


def get_src(all_url):
    src_list = []
    response = requests.get(all_url, headers=ua).text
    html = response.encode('iso-8859-1').decode('gbk')

    tree = etree.HTML(html)

    src = tree.xpath('//ul[@class="clearfix"]/li/a/@href')
    name = tree.xpath('//ul[@class="clearfix"]/li/a/b/text()')

    # 图片的地址
    for path in src:
        path = 'https://pic.netbian.com' + path
        src_list.append(path)
    # 图片的名字
    for n in name:
        name_list.append(n)
    return src_list


def get_img(img_url):
    data_list = []
    for path in get_src(img_url):
        time.sleep(1)
        src = requests.get(path, headers=ua).text
        html = etree.HTML(src)

        data = html.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        data = 'https://pic.netbian.com' + data
        data_list.append(data)
        print(data)
    return data_list


def write(file, img):
    global index
    if not os.path.exists(file):
        os.mkdir(file)
    with open(file + '/' + name_list[index] + '.jpg', 'wb') as f:
        f.write(img)
    index += 1


def main(file, pages):
    global url
    for page in range(pages, pages + 5):
        for contents in get_img(url.format(page)):
            img = requests.get(contents, headers=ua).content
            write(file, img)


if __name__ == '__main__':
    print('爬取开始...')

    main('动漫壁纸5', 20)

    print('爬取结束')
