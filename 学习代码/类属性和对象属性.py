class Person(object):
    types = '人类'  # 这个属于类属性

    def __init__(self, name, age):  # 对象属性
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p1 = Person('zhangsan', 18)

# 用字典的方式打印对象p1中的属性
print(p1.__dict__)

# 类属性能通过类获得,也可以通过对象获得
print(Person.types)
print(p1.types)

# 只能通过类修改，不能通过对象修改
Person.types = '非人类'
p1.types = '人造人'  # 这里是创建一个新的对象属性
print(p1.__dict__)
print(Person.types)

# 用 [] 设置属性就是调用__setitem__方法
p1['name'] = 'lisi'
print(p1.__dict__)

# 用 [] 得到属性就是调用__getitem__方法
print(p1['name'])

print('---------------------------------------')
x = p1.__dict__
print(x)

x['name'] = 'wangwu'
print(x)
