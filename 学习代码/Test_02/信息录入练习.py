# 信息录入
persons = [{'姓名': '陈学平', '年龄': 19},
           {'姓名': '徐国灏', '年龄': 19},
           {'姓名': '王晶', '年龄': 18}]

names = input('请输入你的姓名:')
for person in persons:
    # print(person)
    if person['姓名'] == names:
        print('您输入的姓名已存在')
        break
else:
    new_person = {'姓名': names}
    age = int(input('请输入您的年龄:'))
    new_person['年龄'] = age
    persons.append(new_person)
    print('添加成功！')
print(persons)

# 字典推导式
dicts = {'a': 100, 'b': 200, 'c': 300}
dicts = {v: k for k, v in dicts.items()}
print(dicts)
