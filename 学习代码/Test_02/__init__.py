a = "1a2c"
b = int(a,16)
print(b * 2)
print('hello' * 2)

num1 = int(input('第一个数：'))
num2 = int(input('第二个数：'))
x = num1 if num1>num2 else num2     #三元运算符
print('较大的数是：',x)

#逻辑运算符的优先级：not>and>or

for i in range(3):
    year = int(input('请输入一个年份来判断是否是闰年：'))
    if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
        print('是闰年')
    else:
        print('不是闰年')