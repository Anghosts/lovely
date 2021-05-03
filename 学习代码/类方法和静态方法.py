class Person(object):
    city = '长沙'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + '正在吃' + food)

    # 如果一个方法没有用到实例对象的任何属性，我们可以把它定义为静态方法
    @staticmethod
    def demo():
        print('good')

    # 如果一个方法只用到了类属性，我们可以把它定义为类方法
    @classmethod
    def test(cls):
        print(Person.city)


p1 = Person('张三', 18)
p2 = Person('李四', 17)

p2.eat('面')  # 可以通过实例对象访问方法
Person.eat(p1, '屎')  # 也可以通过类对象访问

# 静态方法的访问
p1.demo()
Person.demo()

# 类方法的访问
p1.test()
Person.test()
