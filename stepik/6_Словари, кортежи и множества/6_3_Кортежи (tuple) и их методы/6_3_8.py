import sys

t='''Главная home
Python learn-python
Java learn-java
PHP learn-php'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))
p = (" ".join(lst_in)).split()
menu = ()
for i in range(0, len(p), 2):
    menu = menu + (tuple(p[i:i+2]),)
print(menu)