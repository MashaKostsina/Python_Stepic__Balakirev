a = int(input())
lst = [[0]*a for i in range(a)]
for i in range(a):
    for j in range(a):
        lst[i][j] = i
for k in lst:
    print(*k)