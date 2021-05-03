'''for i in range(10):
    s=input('请输入你的用户名(只能是字母)\n')
    if s.isalpha():
        print('格式正确！')
    else:
        print('格式错误！')'''

def coco(n): #函数
    if n==1:
        return 1
    else:
        return n*coco(n-1)

print(coco(6))
print('----------------------------------')

for i in range(1,7):
    print(coco(i))