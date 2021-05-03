import random

num1 = 0
for i in range(101):
    num1 += i
print(num1)

num2 = 0
for p in range(37, 987, 3):
    num2 += p
print(num2)

num3 = random.randint(1, 1000)
for k in range(1001):
    if k == num3:
        print('随机数：', num3, '\n查找数：', k)
        break
