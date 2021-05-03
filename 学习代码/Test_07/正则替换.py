import re

t = 'dsaewq32dsa12312dfgdg321hjhg33dg'

print(re.sub(r'\d', 'X', t))
print(re.sub(r'\d+', '', t))


def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


# 在sub内部调用 test 方法时，会把第一个匹配到的值以re.Match的格式传参
print(re.sub(r'\d+', test, 'hello 05 world 99'))   # test 会自动调用
