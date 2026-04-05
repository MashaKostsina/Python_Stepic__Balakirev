t = ()
new = ()
for i in list(map(int,input().split())):
    t = t + (i,)
for n, i in enumerate(t):
    if t.count(i) > 1:
        if n not in new:
                new = new + (n,)
print(*new)