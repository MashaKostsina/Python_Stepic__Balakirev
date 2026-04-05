def get_len(str):
    return str, len(str)

cities = list(input().split())
d = {get_len(x)[0]: get_len(x)[1] for x in cities}

a = sorted(d, key=d.get)
print(*a)