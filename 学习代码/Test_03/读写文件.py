import csv

# 让用户输入幸运数字，并将这些数字保存到文本文件中
num = input("请输入您的幸运数字：")
f = open('D:/tesa.txt', "w+")
f.write(num)     # 将内容写入文件
f.close()   # 关闭文件

f = open('D:/tesa.txt', 'r')
data = f.read()     # 将文件里的内容读取为一个字符串
f.close()
print(data)

f = open('D:/tesa.txt', "a")
f.write('\n你好，世界！')
f.close()

# 写入
with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City"])
    writer.writerow(["Craig Lou", "Taiwan"])
# 读取
with open("test.csv", mode="r", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    for po in reader:
        print(po)

# 'r'	默认模式，即只读模式
# 'w'	写入模式。如果文件不存在，则创建一个文件
# 'x'	创建新文件，如果文件存在，则操作失败
# 'a'	追加模式，如果文件不存在，则创建一个文件
# 'b'	以二进制模式打开文件
# '+'	读写模式， 适合跟新文件
