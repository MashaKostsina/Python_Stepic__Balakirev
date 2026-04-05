def get_str(a, tag="h1"):
    return  f'<{tag}>{a}</{tag}>'

c = input()
print(get_str(c))
print(get_str(c, "div"))