n = int(input())
answer = ""
p = []
for i in range(1, n):
    if n % i == 0 and i != 1:
        p.append(i)
    if len(p) > 0:
        answer = "НЕТ"
    else:
        answer = "ДА"
print(answer)