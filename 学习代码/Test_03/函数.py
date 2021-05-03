def rap(num1, num2):
    num1, num2 = num2, num1
    print('num1 = {}, num2 = {}'.format(num1, num2))
    return num1, num2


def add(iter1):
    j = 0
    for i in iter1:
        j += i
    return j


a = 3
b = 2
rap(a, b)
print('a = {}, b = {}'.format(a, b))
print("==>>", add(range(1, 21)))

# 匿名函数
# lambda [arg1,......,args]:....;
fei = lambda num1, num2: num1 + num2
print(fei(1, 2))


# 用函数作为函数的参数
def calc(a, b, fn):
    x = fn(a, b)
    return x


def add2(x, y):
    return x + y


def add3(x, y):
    return x - y


num = calc(2, 7, add3)
print(num)

print(calc(1, 2, lambda x, y: x + y))
