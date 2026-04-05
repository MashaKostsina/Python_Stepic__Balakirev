lst_in = [[2, 3, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
answer = "ДА"
for i in range(len(lst_in)):
    for j in range(i+1, len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            answer = "НЕТ"
            break
print(answer)