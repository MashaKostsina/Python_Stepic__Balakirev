cities = ()
for i in input().split():
    cities = cities + (i,)
if "Москва" not in cities:
    cities = cities + ("Москва",)
print(*cities)