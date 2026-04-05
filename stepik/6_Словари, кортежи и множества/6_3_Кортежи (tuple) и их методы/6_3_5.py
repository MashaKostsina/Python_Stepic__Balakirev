t = ()
new = ()
for i in list(map(int,input().split())):
    t = t + (i,)
for i in t:
    if i not in new:
        new = new + (i,)
print(*new)
