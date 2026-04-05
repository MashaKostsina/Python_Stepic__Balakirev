a = [1, 2, 4, 8, 16, 32, 64]
n = int(input())
summ = 0
b = []
while n > 0:
    if n // max(a) > 0:
        b.append((n // max(a))* f'{max(a)} ')
    summ = max(a) * (n//max(a))
    n = n - summ
    a.pop()
print(*b, sep="")
