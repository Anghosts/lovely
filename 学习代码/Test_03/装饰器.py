import time


def demo(fn):
    def innter():
        start = time.time()
        fn()
        end = time.time()
        print('耗时%.2f秒' % (end - start))
    return innter


@demo
def demo1():    # 程序的第一步是调用demo()函数，再把demo1作为参数赋给fn，最后得到返回值 innter
    x = 0
    for i in range(1, 100000001):
        x += i
    print(x)


demo1()
# 此时的demo1 并不是原来的demo1，而是 innter，调用demo1，就是调用了 innter()
# 那么之前的demo1去哪了呢，它变成了fn，再第7行调用fn()时，就是调用了第13行的demo1()

