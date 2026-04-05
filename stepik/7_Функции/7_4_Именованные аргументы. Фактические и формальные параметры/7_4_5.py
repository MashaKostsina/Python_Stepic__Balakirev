def get_str(a, tag="h1", up = True):
    if up:
        return f'<{tag.upper()}>{a}</{tag.upper()}>'
    else:
        return f'<{tag}>{a}</{tag}>'


c = input()
print(get_str(c, "div"))
print(get_str(c, "div", False))