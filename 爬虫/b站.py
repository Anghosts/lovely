import gzip
import re
import urllib
import xlwt
from random import choice
from io import BytesIO
from urllib.request import Request, urlopen

from 爬虫 import test

find_all = re.compile(r'投稿(.*)相关推荐', re.S)
find_title = re.compile(r'<h1 title="(.*)" class="video-title">')  # 标题
find_bofang = re.compile(r'<span title="总播放数(\d*)" class="view">')  # 播放人数
find_dm = re.compile(r'<span title="历史累计弹幕数(\d*)" class="dm">')  # 弹幕
find_time = re.compile(r'<span>([0-9]{,5}-\d{,3}-\d{,3}\s.*)</span>')  # 时间
find_pm = re.compile(r'(全站排行榜最高第.*名)')  # 排名
find_dz = re.compile(r'点赞数(.*)" class="like">')  # 点赞人数
find_tb = re.compile(r'投硬币枚数.*</i>\s(.*)')  # 硬币枚数
find_sc = re.compile(r'收藏人数.*</i>(.*)')  # 收藏人数
find_fx = re.compile(r'分享.*</i>(.*)')  # 分享
find_up = re.compile(r'评论.*\n(.*)')  # up
find_gz = re.compile(r'关注.*<span>(.*)</span></span>', re.S)  # 关注


def head():
    headers = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    ]
    ua = {'User-Agent': choice(headers)}
    return ua


data_list = []


# 解析网页
def get_all(path_url):
    import time
    try:
        data = []
        request = Request(path_url, headers=head())
        time.sleep(1)
        response = urlopen(request)
        html = response.read()

        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode('utf-8')

        all_html = re.findall(find_all, html)
        if not all_html:
            return
        else:
            all_html = all_html[0]

        bv_num = path_url.split('/')
        if not bv_num:
            data.append(' ')
        else:
            data.append(bv_num[-1])

        title = re.findall(find_title, all_html)
        data.append(title)

        bf = re.findall(find_bofang, all_html)  # 播放人数
        data.append(bf)

        dm = re.findall(find_dm, all_html)
        data.append(dm)

        time = re.findall(find_time, all_html)
        data.append(time)

        top = re.findall(find_pm, all_html)
        if not top:
            data.append(' ')
        else:
            data.append(top)

        dz = re.findall(find_dz, all_html)
        data.append(dz)

        tb = re.findall(find_tb, all_html)
        tb = re.sub(" ", "", str(tb[0]))
        data.append(tb)

        sc = re.findall(find_sc, all_html)
        data.append(sc)

        fx = re.findall(find_fx, all_html)
        data.append(fx)

        up = re.findall(find_up, all_html)
        if len(up) == 1:
            up = re.sub(" ", "", str(up[0]))
            data.append(up)
        elif len(up) == 2:
            up = re.sub(" ", "", str(up[1]))
            data.append(up)
        else:
            data.append(' ')

        gz = re.findall(find_gz, all_html)
        if not gz:
            data.append(' ')
        else:
            data.append(gz)

        data_list.append(data)
        return data_list

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        else:
            print(e)


def save_file(all_list, save_path):
    print('保存中...')
    workbook = xlwt.Workbook(encoding='utf8', style_compression=0)
    worksheet = workbook.add_sheet('B站热门', cell_overwrite_ok=True)
    col = ("BV", "标题", "播放量", "弹幕", "发布时间", "B站播放排名", "点赞数", "投币数", "收藏数", "转发量", "UP主", "关注人数")
    for i in range(len(col)):
        worksheet.write(0, i, col[i])
    for j in range(len(data_list)):
        data = all_list[j]
        for k in range(len(col)):
            worksheet.write(j + 1, k, data[k])
    workbook.save(save_path)
    print('保存成功！')


def main():
    url_x = 'https://www.bilibili.com/video/'
    count = 1
    for url in test.BV():
        all_url = url_x + url
        data = get_all(all_url)
        if data:
            print("第%d次成功" % count)
            count += 1
        else:
            print('第%d次爬取失败！' % count)
            count += 1
        # if count == 11:
        #     break

    save_file(data_list, 'B站热门-5.xls')


if __name__ == '__main__':
    main()
