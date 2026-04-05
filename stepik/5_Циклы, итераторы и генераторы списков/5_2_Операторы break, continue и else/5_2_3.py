cities = input().split()
i = 0
m = "ДА"
while i < len(cities):
    if len(cities[i]) <= 5:
        m = "НЕТ"
        break
    i += 1
print(m)
