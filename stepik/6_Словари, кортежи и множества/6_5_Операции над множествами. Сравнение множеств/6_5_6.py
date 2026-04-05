list_1 = input().split()
list_2 = input().split()
s1 = set(list_1)
s2 = set(list_2)

if len(s1-s2) == 0:
    print("ДА")
else:
    print("НЕТ")