a = str(input())
b = iter(a)
for i in range(len(a)):
    print(next(b), end=" ")