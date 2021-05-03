x = 'abcdefghijklmnopqrstuvwxyz'
y = '1234567890'
z = '123456789abcdefg'

h = 'hello-world-java-X-python-c-X-money'
# 可以获取指定字符的下标
print(len(x))

print(x.find('l'))  # 如果不存在结果则为 -1
print(x.index('l'))  # 用index查找，如果不存在会报错
print('-------------------------------------')
print(x.isdigit())  # 判断字符串的内容是否为数字
print(y.isdigit())
print('-------------------------------------')
print(x.isalnum())  # 判断是否由字母或数字组成
print(y.isalnum())
print(z.isalnum())
print('-------------------------------------')
i = h.split('-')  # 将字符串切割成一个列表
print(i)
print(h.split('-', 2))
print(h.rsplit('-', 2))
print('-------------------------------------')
print(h.partition('X'))  # 指定一个字符串作为分隔符，分成三部分
print(h.rpartition('X'))
