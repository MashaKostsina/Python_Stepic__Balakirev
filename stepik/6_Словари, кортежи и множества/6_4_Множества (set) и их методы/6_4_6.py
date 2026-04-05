s = set()
a = input()
while a not in "q":
    s.add(a)
    a = input()
print(len(s))
