person = {'name': 'zhangsan', 'age': 18}
print(person['name'])   # 查找元素
print(person.get('height'))     # 用get方法查找，如果不存在，则返回默认值

# 修改
person['name'] = '李四'
print(person)
# 如果key不存在，则会添加一个新的key-value
person['height'] = 185
print(person)
print('----------------------------------')

# 删除
x = person.pop('age')
print(person)
print(x)
y = person.popitem()
print(person)
print(y)
print('----------------------------------')

# 合并
word1 = {'addr': '湖南', 'height': 167}
word2 = {'name': '王晶', 'age': 18}
word1.update(word2)     # update方法
print(word1)
print('----------------------------------')

# 遍历
for i in word1:
    print(i, ':', word1[i])
print('----------------------------------')

for item in word1.items():
    print(item[0], ':', item[1])
print('----------------------------------')

for i, k in word1.items():
    print(i, ':', k)
