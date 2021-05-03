import re

# . 表示任意字符， * 表示任意数量
# (?P<name>表达式) 可以给分组取个名字
m = re.search(r'(1.*)(2.*)(3.*)(4.*)(?P<XXX>5.*)', '1abcm2nxyzd3sadsad4sadsagff5g')
print(m)

print(m.span())

# 获取匹配到的结果
# print(m.group())

# group 方法表示正则表达式的分组
# 下标从0开始，如果没有分组，默认只有一组
print(m.group(0))   # 表示第0个分组
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(4))
print(m.group('XXX'))   # print(m.group(5))

# 获取所有分组
print(m.groups())
# 获取分组 组成的字典
print(m.groupdict('XXX'))   # print(m.groupdict())

# compile 方法
r = re.compile(r'm.*a')
s = r.search('mdsadsagdsa')
print(s)
