# import sys
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ["Города=about-cities", "Машины=read-of-cars", "Самолеты=airplanes"]
d = dict(items.split('=') for items in lst_in)
menu = {**menu, **d}

print(*sorted(menu.values()))