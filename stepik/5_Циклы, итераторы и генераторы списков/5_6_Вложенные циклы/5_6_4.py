lst_in = [[1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
answer = "ДА"
for i in lst_in:
    for j in i:
        if i[j] == 1 and i[j+1] == 1:
            answer = "НЕТ"
            break
for i in range(1,len(lst_in)-1):
    for j in range(1, len(lst_in[i])-1):
        if lst_in[i][j] == 1:
            summ = lst_in[i-1][j-1] + lst_in[i+1][j+1] + lst_in[i-1][j+1] + lst_in[i+1][j-1]
            if summ >= 1:
                answer = "НЕТ"
                break
for i in range(len(lst_in)):
    for j in range(i+1, len(lst_in)):
        lst_in[i][j], lst_in[j][i] = lst_in[j][i], lst_in[i][j]
for i in lst_in:
    for j in i:
        if i[j] == 1 and i[j+1] == 1:
            answer = "НЕТ"
            break
print(answer)