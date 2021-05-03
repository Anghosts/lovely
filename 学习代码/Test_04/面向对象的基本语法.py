class Student(object):
    __slots__ = ('names', 'ages', 'city')  # 用来规定对象可以存在的属性

    def __init__(self, name, age):
        self.names = name
        self.ages = age

    def hello(self):
        print('我叫' + self.names, ',今年{}岁'.format(self.ages))


s = Student('张三', 18)   # 会自动调用__init__方法，并赋值给属性
s.hello()

s.city = '长沙'  # 可以添加类的属性
print('来自'+s.city)
