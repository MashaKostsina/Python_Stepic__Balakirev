import sys

t='''EvgeniyK: спасибо большое!
LinaTroshka: лайк и подписка!
Sergey Karandeev: крутое видео!
Евгений Соснин: обожаю
EvgeniyK: это повтор?
Sergey Karandeev: нет, это новое видео'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))
p = (" ".join(lst_in)).split()
s = set()
for i in p:
    if ":" in i:
        s.add(i)
print(len(s))