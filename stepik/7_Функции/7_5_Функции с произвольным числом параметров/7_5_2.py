def get_biggest_city(*cities):
    a = ""
    for x in cities:
        if len(x) == max([len(x) for x in cities]):
            a = x
    return a

# def get_biggest_city(*cities):
#     return max(cities, key=len)

print(get_biggest_city("Питер", "Москва", "Самара", "Воронеж"))