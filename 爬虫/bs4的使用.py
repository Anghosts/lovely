from bs4 import BeautifulSoup

with open("b站播放页面.html", "rb") as file:
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")

    # 获取标签的内容，包括标签
    print(bs.title)
    print(bs.div)
    # 获取标签里的内容
    print(bs.title.string)
    # 获取标签里的属性
    print(bs.div.attrs)

    print(bs.head.contents)
