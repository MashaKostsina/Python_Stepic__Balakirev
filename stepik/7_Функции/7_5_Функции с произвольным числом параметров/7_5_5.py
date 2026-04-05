# def str_min(a, b):
#     if a < b:
#         return a
#     else:
#         return b
#
#
# def str_min3(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c
#
# def str_min4(a, b, c, d):
#     if a < b and a < c and a < d:
#         return a
#     elif b < a and b < c and b < d:
#         return b
#     elif c < a and c < b and c < d:
#         return c


def str_min(a,b):
    return a if a < b else b

def str_min3(a, b, c):
    return c if c < str_min(a, b) else str_min(a, b)

def str_min4(a, b, c, d):
    return d if a < str_min3(a, b, c) else str_min(a, b)


print(str_min("значимый", "подвиг"))
print(str_min3("это", "заметный", "подвиг"))
print(str_min4("я", "выполнил", "значимый", "подвиг"))
