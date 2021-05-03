# 水仙花数
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)

print('-'*20)

for j in range(1000, 10000):
    x = j // 1000
    y = j // 100 % 10
    z = (j % 100) // 10
    k = j % 10
    if x**3 + y**3 + z**3 + k**3 == j:
        print(j)

