def wrap_with_tag(tag="h1"):
    def decorator(func):
        def wrapper(s):
            content = func(s)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator

@wrap_with_tag(tag="div")
def to_lower(text):
    return text.lower()

s = input()
print(to_lower(s))