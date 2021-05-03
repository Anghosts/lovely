# ImageDownloader - Muhammed Shokr its amazing

def ImageDownloader(url):
    import os, re, requests

    response = requests.get(url)
    text = response.text

    # print(text)
    p = r'<img.*?src="(.*?)"[^\>]+>'
    p1 = r'<img.*?src="^(//hbimg.huabanimg.com/)?[a-f0-9]+\-?[a-zA-Z0-9]?\_[a-z0-9/]?[a-z/]?(webp)$"'
    p2 = r'(https://.*?/300)'

    img_addrs = re.findall(p2, text)

    for i in img_addrs:
        # os.system("wget {}".format(i))
        print(i)

    return 'DONE'


# USAGE
# Change the URL from where you have to download the image
ImageDownloader(
    "https://www.sevengames.cn/")
