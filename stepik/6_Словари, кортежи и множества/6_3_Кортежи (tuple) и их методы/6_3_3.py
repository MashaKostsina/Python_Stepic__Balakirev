cities = ()
a = input().split()
for i in a:
    cities = cities + (i,)
if "Ульяновск" in cities:
    del cities
    cities = ()
    for i in a[:(len(a)+1)]:
        if i == "Ульяновск":
            a.remove(i)
        else:
            cities = cities + (i,)
print(*cities)