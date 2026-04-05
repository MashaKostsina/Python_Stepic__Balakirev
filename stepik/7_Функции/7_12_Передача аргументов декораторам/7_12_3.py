t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# ✅ Декоратор с параметром chars
def replace_and_collapse(chars="?!:;,. "):
    def decorator(func):
        def wrapper(s):
            result = func(s)
            new_result = ''
            prev = ''
            for ch in result:
                if ch in chars or ch == '-':
                    if prev != '-':
                        new_result += '-'
                        prev = '-'
                else:
                    new_result += ch
                    prev = ch
            # удаляем дефис в начале и в конце
            return new_result
        return wrapper
    return decorator

# ✅ Функция транслитерации
@replace_and_collapse(chars="?!:;,. ")
def transliterate(text):
    text = text.lower()
    result = ''
    for ch in text:
        if ch in t:
            result += t[ch]
        else:
            result += ch
    return result

# ✅ Чтение строки и вызов
s = input()
print(transliterate(s))