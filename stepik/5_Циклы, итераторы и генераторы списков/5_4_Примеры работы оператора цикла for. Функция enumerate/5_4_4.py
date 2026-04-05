num = list(map(int,input().split()))
res = []
for i, d in enumerate(num):
    res.append(d**2)
print(*res)