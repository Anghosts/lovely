'''
#水仙花数
for i in range(100,1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)

#求质数
for i in range(2,101):
    flag = True
    for j in range(2,int(i ** 0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)

for i in range(2,101):
    num = 0
    for j in range(2,i):
        if i % j ==0:
            num += 1
            break
    if not(num):
        print(i,'是质数')
'''
# 斐波那契数列
n = int(input('请输入您要第几个斐波那契数:'))
num1 = 1
num2 = 1
for i in range(0, n - 2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)

# 珠峰问题，假设一张纸的厚度为0.08mm，则珠峰的高度为8848.13m，问一张纸需要折几次才能达到珠峰的高度？
height = 0.08 / 1000
count = 0
while True:
    height += height
    count += 1
    if height >= 8848.13:
        break
print(count, '次')
