num = list(map(int,input().split()))
for i in range(len(num)-1):
    for j in range(len(num)-1-i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(*num)





