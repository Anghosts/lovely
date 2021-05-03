name = list(('王晶', '陈学平', '柏鑫', '毛杰'))
print(name)

name.append('李云涛')  # 在列表的最后，插入一个元素
name.insert(4, '钱永盛')  # 在列表指定的位置，插入一个元素
print(name)

name1 = ['郑文强', '郑会军']
name.extend(name1)  # 将可迭代对象 name1 中的元素添加到 name 中
print(name)

x = name.pop(6)  # 删除并返回一个数据，可指定下标
print(x)
print(name)

name.remove('郑会军')  # 删除指定的元素，如果不存在，则报错
print(name)
name.append('徐国灏')

for i in name:  # 遍历
    print(i)

name.clear()    # 删除全部元素
