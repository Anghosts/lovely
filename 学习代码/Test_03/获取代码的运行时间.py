import time


# start = time.time()  # 获取当前时间的时间戳
#
# x = 0
# for i in range(1, 100000000):
#     x += i
# print(x)
# time.sleep(3)  # 可以让代码停 3 秒
# end = time.time()  # 再获取
#
# print('运行时间为%.2f秒' % (end - start))

# 优化
def times(fn):
    start = time.time()
    fn()
    end = time.time()
    print('运行时间为%.2f秒' % (end - start))


def add():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)


times(add)

# 装饰器的简单使用
# def demo(fn):
#     def demo1():
#         print('demo1被调用了')
#         fn()
#     def demo2():
#         print('demo2被调用了')
#         fn()
#     return demo1
#
#
# @demo
# def add():
#     for i in range(1, 21):
#         print(i)
#
#
# add()
