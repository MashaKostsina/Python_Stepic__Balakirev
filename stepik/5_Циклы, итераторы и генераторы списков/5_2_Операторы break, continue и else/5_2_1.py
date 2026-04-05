p = [0] * 10
i = 0
while i < len(p):
    n = int(input())
    p.insert(n, 1)
    p.pop(n + 1)
    if p[n] == n:
        continue
    if p.count(1) == 5:
        break
    i += 1
print(*p, end=" ")