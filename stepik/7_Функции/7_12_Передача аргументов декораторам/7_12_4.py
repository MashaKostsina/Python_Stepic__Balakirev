from functools import wraps


def summarize(func):
    @wraps(func)
    def wrapper(arg):
        numbers = func(arg)
        return sum(numbers)
    return wrapper


@summarize
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))