N = int(input())
lst = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(i,i+1):
        lst[i][j] = 1
for k in lst:
    print(*k)