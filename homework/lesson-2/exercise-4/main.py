# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# ввод данных
user_value = input('Введите строку из нескольких слов, разделённых пробелами: ')

# вывод
i = 1
for v in user_value.split(sep=' '):
    print(f'{i}. {v[:10]}')
    i += 1