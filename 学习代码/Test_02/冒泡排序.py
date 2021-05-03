nums = [1, 5, 3, 6, 8, 7, 9, 2, 4]

# nums.sort(reverse=True)
# n = sorted(nums)
# print(n)
# print(nums)

# 冒泡排序
i = 0
count = 0
while i < len(nums) - 1:
    for n in range(0, len(nums) - 1 - i):  # while n < len(nums) - i:
        count += 1
        flag = True
        if nums[n] > nums[n + 1]:
            flag = False
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
    if flag:
        break
    i += 1

print(nums)
print(count)
