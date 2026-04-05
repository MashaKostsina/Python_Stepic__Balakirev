a = int(input())
res = []
k = 0
answer = []
for i in range(2, a):
    for j in range(2, a):
        if i % j == 0:
            res.append(i)
for i, d in enumerate(res):
    k = res.count(d)
    if k == 1:
        answer.append(d)
print(*answer)