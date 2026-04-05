lst = input()
lst = [[x for x in row.split("=")] for row in lst.split()]
d = dict(lst)
flag = "ДА"
for i in d:
    if 'house' in d and 'True' in d and '5' in d:
        flag = "ДА"
    else:
        flag = "НЕТ"
print(flag)
