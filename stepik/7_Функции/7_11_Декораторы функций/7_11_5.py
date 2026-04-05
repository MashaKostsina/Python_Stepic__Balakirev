# Словарь транслитерации
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# Декоратор
def dash_cleaner(func):
    def wrapper(s):
        result = func(s)
        cleaned = ''
        last_char = ''
        for ch in result:
            if ch == '-' and last_char == '-':
                continue  # пропускаем повторный дефис
            cleaned += ch
            last_char = ch
        return cleaned
    return wrapper

# Функция с транслитерацией
@dash_cleaner
def transliterate(text):
    text = text.lower()
    result = ''
    for ch in text:
        if ch in t:
            result += t[ch]
        elif ch.isalpha():
            result += ch
        elif ch in " :;.,_":
            result += '-'
        else:
            result += ch
    return result

# Получение строки и вызов
s = input()
print(transliterate(s))
