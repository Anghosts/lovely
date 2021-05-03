class Person(object):
    __count = 0

    def __init__(self, name, age):
        Person.__count += 1
        self.name = name
        self.age = age

    @classmethod
    def get__count(cls):
        return cls.__count


p1 = Person('张三', 20)
p2 = Person('李四', 18)

print('个数为 {} 个'.format(Person.get__count()))
