# 查找最大数，并找出下标
# nums = [6, 7, 4, 1, 3, 2, 5, 8]
#
# i = 0
# x = nums[0]
# index = 0
# while i < len(nums):
#     if nums[i] > x:
#         x = nums[i]
#         index = i
#     i += 1
# print('最大数是%d,下标是%d' % (x, index))
# print(x, nums.index(x))

names = ['hello', 'world', '', '', 'good', '', 'yes', '']
names2 = []
# 删除空字符串
for name in names:
    if name != '':
        names2.append(name)
names = names2
print(names)

# 列表推导式
nums = [i for i in range(10)]
print(nums)

nums2 = [i for i in range(10) if i % 2]
print(nums2)

nums3 = [(x, y) for x in range(1, 4) for y in range(10, 15)]
print(nums3)


nums4 = [i for i in range(1, 51)]
print(nums4)
nums5 = [nums4[j: j + 3] for j in range(0, 50, 3)]  # 切片
print(nums5)

