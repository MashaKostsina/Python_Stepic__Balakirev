names_initial = input().split()


def filter_by_length(*args, min_length=0, max_length):
    return [i for i in args if min_length <= len(i) <= max_length]

names_result = filter_by_length(*names_initial, min_length=5, max_length=9) 