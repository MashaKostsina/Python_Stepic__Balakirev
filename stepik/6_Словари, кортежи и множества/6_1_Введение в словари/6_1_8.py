import sys

t='''ustanovka-i-zapusk-yazyka
ustanovka-i-poryadok-raboty-pycharm
peremennyye-operator-prisvaivaniya-tipy-dannykh
arifmeticheskiye-operatsii
ustanovka-i-poryadok-raboty-pycharm'''

sys.stdin.readlines=t.splitlines
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}
for i in lst_in:
    if i not in d:
        d[i] = f'HTML-страница для адреса {i}'
        print(d[i])
    else:
        print(f'Взято из кэша: {d[i]}')
