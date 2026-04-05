lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
a = [i for j in lst_in[::-1] for i in j[::-1]]
print(*a)