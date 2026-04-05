marks = input().lower().split()
b = [marks.count(x) for x in marks]
d = {marks[x]:b[x] for x in range(len(marks))}
print(d.get("и", 0))

# l = input().lower().split()
# print({k:l.count(k) for k in l}.get('и', 0))