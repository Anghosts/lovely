file = open(r'E:\视频\Python教程2020版 完全入门 达到Python工程师水平~连载中\字符串.mp4', 'rb')

# print(file.readline())  # 只读一行
# print(file.readlines())     # 将读取每一行的数据分成一个列表

# print(file.read())
while True:
    count = file.read(1024)
    if not count:
        break
    print(count)

file.close()
