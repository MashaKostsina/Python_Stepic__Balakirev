def func_decorator(func):
    def wrapper(*args, **kwargs):
        tupl = func(*args, **kwargs)
        return dict(zip(tupl[0], tupl[1]))

    return wrapper


@func_decorator
def get_list(string1, string2):
    return [string1.split(), string2.split()]


a = input()
b = input()
d = get_list(a, b)

print(*sorted(d.items()))
