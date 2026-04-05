def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


digs = list(map(int, input().split()))

print(*filter_lst(digs))
print(*filter_lst(digs, lambda a: a < 0))
print(*filter_lst(digs, lambda a: a >= 0))
print(*filter_lst(digs, lambda a: 3 <= a <= 5))
