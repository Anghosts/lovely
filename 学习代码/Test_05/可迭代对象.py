class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 每一次for...in都会调用__next__方法
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止


d = Demo(10)

# for...in 循环的本质就是调用可迭代对象的__iter__方法，获取到这个方法的返回值
# 这个返回值需要是一个对象，然后再调用这个对象的__next__方法
for i in d:
    print(i)
