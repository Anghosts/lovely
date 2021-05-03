# 让用户输入任意数量的银行卡号，然后将这些银行卡号存储到列表中。 当用户输入完成后，将这个列表转换为不可变集合，并打印出该集合
flag = 1
nums = []
while flag:
    num = input('请输入银行卡号：')
    if num.isdigit():
        nums.append(num)
    else:
        print('银行卡全部由数字组成，请注意格式！')
    flag = int(input('是否继续输入？(1 继续，0 退出)'))
for i in range(0, len(nums)):
    fro = frozenset([nums[i]])
    print(fro)
