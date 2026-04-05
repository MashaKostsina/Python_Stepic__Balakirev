def get_even(*args):
    return [x for x in args if x%2 == 0]


print(*(get_even(45, 4, 8, 11, 12, 0)))
# def os_path(disk, *args, sep='\\', **kwargs):
#     args = (disk,) + args
#
#     if 'trim' in kwargs and kwargs['trim']:
#         args = [x.strip() for x in args]
#
#     path = sep.join(args)
#     return path
#
#
# p = os_path("F:", "~stepik.org",
#             "Добрый, добрый Python (Питон)",
#             "39\\p39. Функции.docx",
#             sep='/', trim=True
# )
# print(p)