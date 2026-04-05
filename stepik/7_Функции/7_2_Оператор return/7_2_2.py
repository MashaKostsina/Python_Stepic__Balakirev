def is_triangle(a, b, c):
    return True if a < b + c and b < a + c and c < a + b else False


print(is_triangle(2, 3, 7))