def get_rect_value(a, b, tp=0):
    if tp == 0:
        return 2 * (a + b)
    else:
        return a * b


print(get_rect_value(2, 3, 1))