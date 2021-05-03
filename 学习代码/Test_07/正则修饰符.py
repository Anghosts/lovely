import re

# re.S  让 . 匹配换行
# re.I  匹配大小写
# re.M  让 $ 匹配到换行

# \w 表示的是字母 数字 下划线，+ 出现一次以上，$ 以指定的内容结尾

z = re.findall(r'\w+$', 'i am boy\n you are girl\n he is man', re.M)
print(z)
