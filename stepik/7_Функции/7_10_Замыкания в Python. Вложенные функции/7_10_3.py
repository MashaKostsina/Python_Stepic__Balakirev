def get_string():
    def new_string(string):
        return f'<h1>{string}</h1>'

    return new_string


cnt = get_string()
k = input()

print(cnt(k))
