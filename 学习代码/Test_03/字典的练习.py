# 询问用户名字和年龄，根据回答创建一个包含这些“键-值”对的字典，并尝试输出字典信息。
# name = input('请输入你的用户名：')
# age = int(input('请再输入你的年龄：'))
# person = {name: age}
# # person[name] = age
# print(person)

# 使用for循环，将pizza字典中“键”'ingredients'对应的所有配料信息
pizza = {'ingredients': ['cheese', 'sausage', 'peppers']}
for i in pizza['ingredients']:
    print(i)

print('-'*30)
# 默认遍历key
person2 = {"name": "John", "age": 26}
for i in person2:
    print(i)

print('-'*30)
# 只遍历value
for i in person2.values():
    print(i)

print('-'*30)
# 遍历key-value
for key, value in person2.items():
    print(key, value)
