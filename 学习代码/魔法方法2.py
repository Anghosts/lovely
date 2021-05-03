class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):  # == 运算符
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):    # > 运算符
        pass


p1 = ('张三', 18)
p2 = ('张三', 18)

# == 运算符本质就是调用__eq__方法，获取__eq__方法的返回结果
print(p1 == p2)

# != 本质就是调用__ne__方法，或者__eq__方法取反
print(p1 != p2)
