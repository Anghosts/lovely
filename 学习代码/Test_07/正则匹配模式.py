import re

# \s 表示任意的空白字符
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\n', 'hello\nworld'))  # 换行
print(re.search(r'\t', 'hello\tworld'))  # 制表符

# \S 表示非空白字符
print(re.search(r'\S', '\t\n\t   name'))

# [] 表示可选项范围 [x-y] 从x到y区间，包含x和y
m1 = re.search(r'a[0-5]+z', 'adca0123zxyz')
m2 = re.search(r'a[a-z]+z', 'adcazxyz')
print(m1, m2)

# a<= value <=c 或者 x<= value <=z 或者 0<= value <=9 或者 value = '$' 或者 value = 'd'
m3 = re.search(r'a[a-cx-z0-9$d]+z', 'ad$cazxy0123456z')
print(m3)

# | 表示或者,()里为可选值
m4 = re.search(r'a(b|c|d|e)f', 'abcdaef')
print(m4)

# {} 用来像限定前面元素出现的次数
# {n} 表示前面元素出现n次
# {n,} 表示前面元素出现n次以上
# {,n} 表示前面元素出现n次以下
# {m,n} 表示前面元素出现 m 到 n 次
m5 = re.search(r'go{,2}d', 'good')  # m5 = re.search(r'go{2,}d', 'goooood')
print(m5)

# * 表示出现任意次数(0次及以上)   {0,}
# + 表示前面元素出现任意次数 至少一次   {1,}
# ? 表示前面元素出现任意次数 最多一次   {,1}

# ^ 表示以指定内容开头，$ 表示以指定内容结尾，在[]里还可以表示取反
m6 = re.search(r'^a.*z$', 'efg\nabc xyz\nopq', re.M)
print(m6)

