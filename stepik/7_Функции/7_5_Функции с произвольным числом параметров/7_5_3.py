def get_data_fig(*side, **kwargs):
    p = (sum(side),)
    for i in ['tp', 'color', 'closed', 'width']:
        if i in kwargs:
            p = p + (kwargs[i],)
    return p


print(*(get_data_fig(1, 2, 3, 4, 3, 2, 4, tp = True, closed = False, width = 3.6)))