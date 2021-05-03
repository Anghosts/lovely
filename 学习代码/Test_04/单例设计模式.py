class Person:
    __x = None
    __is_first = True

    def __new__(cls, *args, **kwargs):
        if cls.__x is None:
            cls.__x = object.__new__(cls)     # 申请内存空间
        return cls.__x

    def __init__(self, name, age):
        if self.__is_first:
            self.name = name
            self.age = age

    def eat(self):
        print(self.name + '在吃')


# 创建对象会自动调用__new__方法申请内存空间
# 如果重写了__new__方法，需要手动申请
p1 = Person('张三', 18)
p2 = Person('李四', 20)

print(p2.name, p2.age)

print(p1 is p2)
