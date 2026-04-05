things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
N = int(input())*1000
a = 0
item = []
while N != 0:
    if len(things) != 0:
        max_key = max(things, key=things.get)
        a = things.get(max_key)
        if N >= a:
            item.append(max_key)
            N = N - a
            things.pop(max_key)
        else:
            things.pop(max_key)
    else:
        break
print(*item)

