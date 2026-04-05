names = input().lower().split()
i = 0
m = "НЕТ"
while i < len(names):
    if names[i][0] == names[i][-1]:
        m = "ДА"
        break
    i += 1
print(m)