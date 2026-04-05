import sys

t='''Мария
Елена
Екатерина
Александр
Елена
Мария'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))
s = set(lst_in)
print(len(s))