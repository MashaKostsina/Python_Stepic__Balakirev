text = input()
symbols = input()

def count_chars(s, chars, *, return_type=tuple, ignore_case=True):
    counts = []
    for i in chars:
        if ignore_case:
            i = i.lower()
            s = s.lower()
            counts.append(s.count(i))
        else:
            counts.append(s.count(i))
    return return_type(counts)

result = count_chars(text, symbols, return_type=set, ignore_case=False)
print(result)