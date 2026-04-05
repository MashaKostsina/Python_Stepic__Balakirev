s = set()
for i in input():
    if i.isdigit():
        s.add(i)
if len(s) == 0:
    print("НЕТ")
else:
    print(*sorted(s))