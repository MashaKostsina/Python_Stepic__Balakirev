a = input().split()
d = {}
for i in a:
    if i[0:2] == "+2":
        d.setdefault('+2', []).append(i)
    elif i[0:2] == "+5":
        d.setdefault('+5', []).append(i)
    elif i[0:2] == "+6":
        d.setdefault('+6', []).append(i)
    elif i[0:2] == "+7":
        d.setdefault('+7', []).append(i)
print(*sorted(d.items()))

