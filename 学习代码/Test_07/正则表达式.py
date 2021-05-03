import re
from collections.abc import Iterable

# 在字符串中查找 'hello'
# 从头开始匹配，如果匹配失败，则返回None，只查找一次

m1 = re.match(r'hello', 'hello world good yes')
print(m1)

# 匹配整个字符串，只查找一次
m2 = re.search(r'hello', 'hello world good yes')
print(m2)

# 查找所有匹配的字符串，返回的结果是一个可迭代对象
m3 = re.finditer(r'x', 'abcxefxghxsijkxlmnopqrstxxyzx')
print(m3)
# print(isinstance(m3, Iterable))
#
# for i in m3:
#     print(i)

# 把所有匹配到的字符串放入一个列表中
m4 = re.findall(r'x\d+', 'abcx3efx32ghxsijkx1lmnopqrstxx22yzx5')
print(m4)

# 完整匹配，字符串需要完全满足正则规则，否则返回None
m5 = re.fullmatch(r'hello world', 'hello world')
print(m5)
