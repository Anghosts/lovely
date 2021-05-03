'''for i in 'helloworld':
    print(i)'''

'''for k in range(1,101):
    if k%2==0:
        print(k)'''

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()

lis=list(['https://www.baidu.com/',])
print(lis)
print(lis[::1])
for k in lis:
    print(k)