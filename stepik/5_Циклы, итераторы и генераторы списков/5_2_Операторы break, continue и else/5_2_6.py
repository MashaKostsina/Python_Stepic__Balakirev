n = int(input())
i = 1
p = 0
while i <= n:
    p = i**2
    if p > n:
        break
    i += 1
print(i)