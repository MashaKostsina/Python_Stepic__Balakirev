writers = input().split()
def most_popular(people, *, case_sens=False):
    counts = {}
    for person in people:
        key = person if case_sens else person.lower()
        if key in counts:
            counts[key][1] += 1
        else:
            counts[key] = [person, 1]

    max_count = 0
    result_person = None

    for key, value in counts.values():
        if value > max_count:
            max_count = value
            result_person = key

    return (result_person, max_count)

# writers = ['Пушкин', 'Лермонтов', 'Гоголь', 'Чехов', 'Крылов', 'ЛЕРМОНТОВ', 'Гоголь', 'ЧЕХОВ', 'крылов', 'Пушкин', 'КРЫЛОВ']
result = most_popular(writers, case_sens=True)
print(result)