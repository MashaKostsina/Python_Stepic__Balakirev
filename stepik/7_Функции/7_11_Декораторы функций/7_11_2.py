menu = input()


def show_menu(func):
    def wrapper(*args):
        menu = func(*args)
        [print(f"{i + 1}. {j}") for i, j in enumerate(menu)]

    return wrapper


@show_menu
def get_menu(s):
    return s.split()
