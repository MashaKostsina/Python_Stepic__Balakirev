N = int(input())
zeros = []
for i in range(N):
    zeros.append([0] * N)
for i in range(N):
    for j in range(N):
        zeros[i][j] = 1
        zeros[i][-1] = 5
for i in zeros:
    print(*i)
