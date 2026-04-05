def get_func(tag):
    def inner_func(string):
        nonlocal tag
        return f'<{tag}>{string}</{tag}>'

    return inner_func


a = input()
b = input()
c = get_func(a)
print(c(b))
