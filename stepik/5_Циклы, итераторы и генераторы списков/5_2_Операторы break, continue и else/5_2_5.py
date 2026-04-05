n = int(input())
i = 1
p = []
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        p.append(i)
    if n >= 100:
        print("слишком большое значение n")
        break
    i += 1
print(*p, end=" ")