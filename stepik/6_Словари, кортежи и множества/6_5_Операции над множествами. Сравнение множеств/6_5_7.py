number = int(input())
s = {1, 2, 3, 5, 7}
s2 = {2, 3, 5}
new_set = set()
for i in s:
    if number % i == 0:
        new_set.add(i)
if len(s2 - new_set) == 0:
    print("ДА")
else:
    print("НЕТ")