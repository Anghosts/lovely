class MyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '密码长度必须在{}到{}之间'.format(self.x, self.y)


password = input('请输入您的密码：')
m = 12
n = 6
if n <= len(password) <= m:
    print('密码正确')
else:
    raise MyError(n, m)
