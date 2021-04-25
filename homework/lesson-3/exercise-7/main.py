# 7. Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделённых пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Используйте написанную ранее функцию int_func().

def is_ascii(s):
    return all(65 <= ord(c) <= 122 for c in s)


def is_lower(s):
    return s.islower()


# реализация функции
def int_func(s):
    return s.title()


user_value = ''

while True:
    user_value = input('Введите строку из слов, разделённых пробелами: ')
    values = user_value.split()
    if len(values) > 1:
        for v in values:
            if not is_ascii(v):
                print(f'Ошибка! Слово "{v}" не состоит из латинских букв!')
                break
            elif not is_lower(v):
                print(f'Ошибка! Слово "{v}" не состоит из букв в нижнем регистре!')
                break
        else:
            break
    else:
        print('Ошибка! Строка должна содержать не менее 2-х слов!')

# вывод результата
print(f"Результат вызова функции int_func('{user_value}'): {int_func(user_value)}")
