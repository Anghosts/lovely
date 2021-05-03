import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始为私有属性

    def get__money(self):  # 获取私有属性
        print('{} 查询了余额'.format(datetime.datetime.now()))
        return '余额为：{}元'.format(self.__money)

    def set__money(self, new_money):  # 设置私有属性
        print('修改了余额')
        self.__money = new_money

    def __demo(self):  # 私有方法
        print('我是私有方法')

    def get__demo(self):
        return self.__demo()


p = Person('张三', 18)

# 获取私有属性的方式
print(p._Person__money)

# 可以定义get和set方法来获取
p.set__money(10000)
print(p.get__money())

p.get__demo()
