# 列表生成式
list1 = list(range(1, 31))
print(list1)

# 用列表生成式打印九九乘法表
print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)]))

# list生成式的语法：
# [expr for iter_var in iterable]
# [expr for iter_var in iterable if cond_expr]

# 第一种语法：首先迭代 iterable 里所有内容，每一次迭代，都把 iterable 里相应内容放到iter_var 中，
# 再在表达式中应用该 iter_var 的内容，最后用表达式的计算值生成一个列表。

# 第二种语法：加入了判断语句，只有满足条件的内容才把 iterable 里相应内容放到 iter_var 中，
# 再在表达式中应用该 iter_var 的内容，最后用表达式的计算值生成一个列表。

# 其实不难理解的，因为是 list 生成式，因此肯定是用 [] 括起来的，
# 然后里面的语句是把要生成的元素放在前面，后面加 for 循环语句或者 for 循环语句和判断语句。

list2 = [x for x in range(1, 31)]
print(list2)

list3 = [y for y in range(1, 31) if y % 2 == 0]
print(list3)
