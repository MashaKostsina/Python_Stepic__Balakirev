def sort_list(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)
    return wrapper


@sort_list
def get_list(string):
    lst = list(map(int, string.split()))
    return lst


num = input()
lst = get_list(num)
print(*lst)
