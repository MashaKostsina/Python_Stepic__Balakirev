a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
A = [[row[i] for row in a] for i in range(len(a[0]))]
for row in A:
    print(*row)