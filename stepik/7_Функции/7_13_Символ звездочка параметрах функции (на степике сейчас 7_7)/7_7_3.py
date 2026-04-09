def merge_dicts(*dict1, ignored_keys=None):
    result = {}
    if ignored_keys is None:
        ignored_keys = set()

    for d in dict1:
        for key, value in d.items():
            if key not in ignored_keys:
                result[key] = value  # перезапись значений

    return result

goods = merge_dicts(goods1, goods2, goods3, goods4, ignored_keys=('id', 'date', 'cat_id',))

