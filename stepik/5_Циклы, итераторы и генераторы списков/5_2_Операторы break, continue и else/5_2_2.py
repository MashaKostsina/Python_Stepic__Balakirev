s = 1
d = 1
while d != 0:
    d = int(input())
    if d < 0:
        continue
    if d > 0:
        s *= d
print(s)