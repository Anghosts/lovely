# 用递归算Fibonacci数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fn = fibonacci(8)
print(fn)
