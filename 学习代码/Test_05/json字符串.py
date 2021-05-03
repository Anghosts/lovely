import json

names = ['zhangsan', 'lisi', 'tom', 'tony']
# x = json.dumps(names)   # 将数据转换成为字符串

file = open('names.txt', 'w', encoding='utf8')

# file.write(x)

json.dump(names, file)  # 将数据转换成为字符串，并写入到文件中
file.close()

# json里将数据持久化有两个方法：
# dump
# dumps

# json 反序列化也有两个方法
# loads：将json字符串加载成为python里的数据
# load：读取文件，把数据的内容加载为python里的数据

name = '{"name": "zhangsan", "age": "18"}'

p = json.loads(name)
print(p)

files = open('names.txt', 'r', encoding='utf8')

y = json.load(files)
print(y)
