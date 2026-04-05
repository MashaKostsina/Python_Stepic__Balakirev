n = int(input())
a = 1000
i = 1
while i <=n:
    a = a + (a * 5 / 100)
    i += 1
print(round(a, 2))