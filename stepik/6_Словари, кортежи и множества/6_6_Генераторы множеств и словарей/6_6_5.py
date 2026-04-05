lst_in = ["Пушкин: Сказка о рыбаке и рыбке", "Есенин: Письмо к женщине", "Тургенев: Муму", "Пушкин: Евгений Онегин", "Есенин: Русь"]
lst_new = [x.split(": ") for x in lst_in]
d = dict()
for k,v in lst_new:
    val = d.setdefault(k, set())
    val.add(v)
    d[k] = val

print(d)

# d = {k: {v for a, v in (i.split(": ", 1) for i in lst_in) if a == k}
#      for k in {i.split(": ", 1)[0] for i in lst_in}}

# d = {}
#
# for item in lst_in:
#     author,book = item.split(": ")
#
#     if author not in d:
#         d[author] = set()
#     d[author].add(book)