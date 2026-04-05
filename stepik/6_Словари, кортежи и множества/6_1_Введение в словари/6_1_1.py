lst = input()
lst = [[x for x in row.split("=")] for row in lst.split()]
for i in lst:
    for j in i:
        if j.isdigit():
            i.pop()
            i.append(int(j))
d = dict(lst)
print(*sorted(d.items()))

# d = dict([x.split("=") for x in input().split()])
# for key,value in d.items():
#     d[key] = int(value)
# print(*sorted(d.items()))