import re

# \d 表示数字，等价于[0-9]

# \D 表示非数字，等价于[^0-9]
print(re.search(r'x\D+p', 'xdp123p'))
print(re.search(r'x[^0-9]+p', 'xdp123p'))

# \w 表示字母 数字 下划线，等价于[a-zA-B0-9_],同时包括中文
print(re.findall(r'\w+', 'x-d+p*1_23p'))

# \W 表示\w取反
print(re.findall(r'\W+', 'x-d+p*1_23p'))
