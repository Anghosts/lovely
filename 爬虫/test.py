from random import choice

import requests, re


def BV():
    url = 'https://www.bilibili.com/v/popular/all?spm_id_from=333.851.b_7072696d61727950616765546162.3'
    headers = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla / 5.0(Windows NT 6.1;rv: 2.0.1) Gecko / 20100101Firefox / 4.0.1'
    ]
    ua = {'User-Agent': choice(headers)}

    r = requests.get(url, headers=ua)
    html = r.text

    bv = re.findall(r'"bvid":"(.*?)"', html)
    return bv
