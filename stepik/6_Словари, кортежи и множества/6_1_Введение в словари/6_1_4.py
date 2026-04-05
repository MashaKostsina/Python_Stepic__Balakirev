lst = input()
lst = [[x for x in row.split("=")] for row in lst.split()]
d = dict(lst)
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))