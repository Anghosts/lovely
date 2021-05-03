class Person(object):
    def __init__(self, name, age):
        print('__init__被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，程序会自动调用这个方法
        print('__del__被调用了')

    # 当打印一个对象时，会自动调用__str__方法或者__repr__方法
    def __str__(self):
        return '姓名{}，年龄{}'.format(self.name, self.age)

    def __repr__(self):
        return 'hello'

    def __call__(self, *args, **kwargs):
        # print('__call__被调用了')
        # args 是保存一个元组 (1, 2)
        # kwargs 是保存一个字典 {'fn': lambda x, y: x + y}
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person('张三', 17)
print(p)

n = p(1, 2, fn=lambda x, y: x + y)  # 就是调用对象的__call__方法
print(n)
