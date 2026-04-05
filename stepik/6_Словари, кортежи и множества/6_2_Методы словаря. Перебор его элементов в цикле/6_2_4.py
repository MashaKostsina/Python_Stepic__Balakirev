import sys

t='''3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))
p = (" ".join(lst_in)).split()
d = {}
for i in range(0, len(p), 2):
    if p[i] not in d:
        d[p[i]] = p[i+1]
    else:
        d[p[i]] = d.get(p[i]) + ", " + p[i+1]
for key, value in d.items():
    print(f'{int(key)}: {value}', sep="\n")
