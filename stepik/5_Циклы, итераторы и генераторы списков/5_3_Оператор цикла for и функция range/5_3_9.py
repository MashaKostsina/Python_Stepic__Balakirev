cities = input().lower().split()
letters = []
answer = ""
for i in range(len(cities)):
    letters.append(cities[i][0])
    if cities[i][-1] == 'ь' or cities[i][-1] == 'ъ' or cities[i][-1] == 'ы':
        letters.append(cities[i][-2])
    else:
        letters.append(cities[i][-1])
for i in range(2, len(letters), 2):
    if letters[i] == letters[i-1]:
        answer = "ДА"
    else:
        answer = "НЕТ"
        break
print(answer)
