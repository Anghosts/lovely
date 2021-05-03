def triangles(n):         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in triangles(10):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break
