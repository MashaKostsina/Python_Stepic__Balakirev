lst_in = ["Муму", "Евгений Онегин", "Сияние", "Мастер и Маргарита", "Пиковая дама", "Колобок"]
i = 0
a = []
while i < len(lst_in):
    if " " in lst_in[i]:
        a.append(lst_in[i])
    i += 1
n = 0
while n < len(a):
    if a[n] in lst_in:
        lst_in.remove(a[n])
    n += 1
print(*lst_in)
