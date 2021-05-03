import csv

file = open('demo2.csv', 'w', encoding='utf8', newline='')
# 写入
w = csv.writer(file)
w.writerow(['name', 'age', 'score', 'city'])

file.close()

# 读取
files = open('demo2.csv', 'r', encoding='utf8', newline='')
r = csv.reader(files)
for i in r:
    print(i)

files.close()
