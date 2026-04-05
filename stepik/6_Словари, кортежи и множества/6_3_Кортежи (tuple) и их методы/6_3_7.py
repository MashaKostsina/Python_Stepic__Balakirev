t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input())
t2 = ()
t3 = ()
for i, k in enumerate(t[0:n]):
    for j, l in enumerate(k[0:n]):
        t2 = t2 + (l,)
for i in range(0, len(t2), n):
    t3 = t3 + (t2[i:i+n],)
for k in t3:
    print(*k)