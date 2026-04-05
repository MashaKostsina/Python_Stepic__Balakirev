import sys

t='''+71234567890 Сергей
+71234567810 Сергей
+51234567890 Михаил
+72134567890 Николай'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))


p = (" ".join(lst_in)).split()
d = {}
for i in range(1, len(p), 2):
    if i not in d:
        d.setdefault(p[i], []).append(p[i-1])
print(*sorted(d.items()))


