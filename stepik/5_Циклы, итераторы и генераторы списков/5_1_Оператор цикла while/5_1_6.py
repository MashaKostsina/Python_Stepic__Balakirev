a = int(input())
summa = 1
s = 0
while a != 0:
    s = a % 10
    summa *= s
    a = a // 10
print(summa)