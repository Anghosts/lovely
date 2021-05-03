file = open("demo1.txt", "w+")
num = input('输入点东西: ')
file.write(num)     # 写入

file = open('demo1.txt', 'r')

print(file.read())  # 读文件

file.close()


