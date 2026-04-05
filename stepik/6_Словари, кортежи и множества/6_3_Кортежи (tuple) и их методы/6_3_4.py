name = ()
lst = []
for i in input().lower().split():
    name = name + (i,)
for i in name:
    if "ва" in i[:]:
        lst.append(i)
print(*lst)