def is_large(str):
    return False if len(str) < 6 else True

cities = list(input().split())
lst = [x for x in cities if is_large(x)]

print(*lst)