from functools import reduce
studend = [
    {'name': 'zhangsan', 'age': 18, 'height': 167},
    {'name': 'lisi', 'age': 9, 'height': 98},
    {'name': 'tom', 'age': 27, 'height': 179}
]
studend.sort(key=lambda ele: ele['age'])
print("按年龄从小到大是：")
for i in studend:
    print(i['name'])

# 其它三个方法
# filter方法，作用是过滤，对可迭代对象继续过滤
ages = [23, 32, 18, 17, 13, 5, 58]

# 第一个参数为函数，第二个为可迭代对象
x = filter(lambda ele: ele > 18, ages)  # 结果为filter类型的对象
for i in x:
    print(i)

# map方法
ages1 = [12, 24, 32, 44, 52]
x1 = map(lambda ele: ele + 2, ages1)
print(list(x1))

# reduce方法
ages2 = [100, 300, 4, 7, 88, 99]
x2 = reduce(lambda ele1, ele2: ele1 + ele2, ages2)
print(x2)
