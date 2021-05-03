f = open(r'E:\视频\Python教程2020版 完全入门 达到Python工程师水平~连载中\字符串.mp4', 'rb')
f2 = open('void.txt', 'wb')

try:
    while True:
        c = f.read(1024)
        f2.write(c)
        if not c:
            break
finally:    # 最终都会执行的代码
    print('文件被关闭了')
    f.close()
    f2.close()
