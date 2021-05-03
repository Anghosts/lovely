# 字符串创建迭代器
str1 = 'hello world'
iter1 = iter(str1)

# 列表创建迭代器
list1 = [1, 2, 3, 4, 5]
iter2 = iter(list1)

# 元组创建迭代器
tuple1 = (6, 7, 8, 9, 0)
iter3 = iter(tuple1)

# for循环遍历迭代器
for i in iter1:
    print(i, end='')

print('\n------------------------')

# next()函数遍历
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break
