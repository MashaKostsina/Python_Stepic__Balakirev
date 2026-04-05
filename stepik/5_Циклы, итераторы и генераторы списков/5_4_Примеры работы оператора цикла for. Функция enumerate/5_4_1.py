a = input()
d = "ра"

for i, d in enumerate(a):
    if a[i:i+2] == "ра":
        print(i, end=" ")
if "ра" not in a[:]:
    print("-1")




