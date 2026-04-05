get_module = lambda x: abs(x) if x < 0 else x

x = float(input())
print(get_module(x))
