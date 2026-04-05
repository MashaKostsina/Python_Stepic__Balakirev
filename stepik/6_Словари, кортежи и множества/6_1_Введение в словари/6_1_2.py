import sys

t='''5=отлично
4=хорошо
3=удовлетворительно'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for i in lst_in:
    for j, k in enumerate(i):
        if k.isdigit():
            d[int(k)] = i[2:]
print(*sorted(d.items()))