print('hello world')
lis = list(['https://www.baidu.com/'])
i=0
b=9
m=123456
r=range(1,10,2)

while i<10:
    s = int(input('请输入密码：'))
    if s==m:
        print('密码正确！')
        print(list(r))
        print(lis)
        break
    else:
        print('密码错误，请重新输入！还可以输入',b,'次')
        b-=1
        i+=1
