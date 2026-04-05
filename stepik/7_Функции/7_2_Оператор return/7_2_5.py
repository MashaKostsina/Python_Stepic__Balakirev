def is_not_even(a):
    return True if a % 2 != 0 else False

lst_d = list(map(int, input().split()))
lst = [x for x in lst_d if is_not_even(x) ]
print(*lst)