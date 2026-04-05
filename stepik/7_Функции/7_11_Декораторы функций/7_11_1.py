def get_sq(width, height):
    s = width * height
    return s

def func_show(func):
    def wrapper (*args):
        func(*args)
        print(f'Площадь прямоугольника: {func(*args)}')
    return wrapper



