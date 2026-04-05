a = input()


def df_decorator(start):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = func(x) + start
            return res

        return wrapper

    return func_decorator


@df_decorator(start=5)
def convert_to_int(str):
    list = map(int, str.split())
    return sum(list)


print((convert_to_int(a)))
