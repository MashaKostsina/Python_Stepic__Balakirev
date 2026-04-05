marks = input().split()
a = [(int(marks[0])+x) for x in range(len(marks)-1)]
b = [x for x in marks[1:]]
d = {a[x]:b[x] for x in range(len(a))}
print(d.get(4))

# marks = input().split()
# d = {int(marks[0]) + index: value for index, value in enumerate(marks[1:])}