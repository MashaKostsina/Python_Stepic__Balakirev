a = input()
b = iter(a)
for i in range(a.index(" ")):
    print(next(b), end="")


