def get_func(tp):
    def inner_func(string):
        nonlocal tp
        if tp == "list":
            lst = list(map(int, string.split()))
        else:
            lst = tuple(map(int, string.split()))
        return lst

    return inner_func


a = input()
b = input()
c = get_func(a)
print(c(b))
