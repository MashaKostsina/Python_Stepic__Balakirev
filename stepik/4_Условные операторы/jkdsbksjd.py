nums = [5, 7, 8, 2, 3]
flag = 9
rtype = []
for i in nums:
    for j in nums:
        if i + j == flag:
            if i not in rtype:
                rtype.append(nums.index(i))
print(*rtype)