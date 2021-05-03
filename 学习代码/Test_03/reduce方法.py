from functools import reduce

# 将列表里的age相加
studend = [
    {'name': 'zhangsan', 'age': 18, 'height': 167},
    {'name': 'lisi', 'age': 9, 'height': 98},
    {'name': 'tom', 'age': 27, 'height': 179}
]


def add(x, y):
    return x + y['age']


x = reduce(add, studend, 0)     # 给定 x 的初始值为 0
print(x)
