import sys

s_in = sys.stdin

# 一直读取用户的输入
while True:
    content = s_in.readline().rstrip('\n')
    if content == '':
        break
    print(content)

# 标准输出
sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('hello')

# 错误输出
sys.stderr = open('stderr.txt', 'w', encoding='utf8')
print(1/0)
