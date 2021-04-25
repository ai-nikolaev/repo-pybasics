# Реализовать функцию int_func(), принимающую слова из маленьких
# латинских букв и возвращающую их же, но с прописной первой
# буквой. Например, print(int_func(‘text’)) -> Text.

# реализация функции
def int_func(s):
    def is_ascii(ss):
        return all(65 <= ord(c) <= 122 for c in ss)

    def is_lower(ss):
        return ss.islower()

    if not is_ascii(s):
        print('Ошибка! Слово должно состоять из латинский букв!')
        return None
    elif not is_lower(s):
        print('Ошибка! Слово должно состоять из маленьких букв!')
        return None
    return s.capitalize()


# вывод
print(int_func('text'))
