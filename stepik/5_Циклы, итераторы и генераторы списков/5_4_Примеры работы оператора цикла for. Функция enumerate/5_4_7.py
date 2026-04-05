num = list(map(float,input().split()))
for i, d in enumerate(num):
    if d < 0:
        num.remove(d)
        num.insert(i, -1.0)
print(*num)