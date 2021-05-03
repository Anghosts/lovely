import re

# 判断用户输入的是否为数字
num = input('请输入一段数字：')
if re.fullmatch(r'\d+(\.?\d+)?', num):
    print(float(num))
else:
    print('不是一个数字')
