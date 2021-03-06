# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введён после нескольких чисел, то
# вначале нужно добавить сумму этих чисел к полученной ранее сумме и
# после этого завершить программу.

# переменная для суммы чисел
r = 0

# вычисление
while True:
    value = input('Введите строку чисел, разделённых пробелом: ')
    try:
        for v in value.split():
            r += int(v)
    except ValueError:
        break
    finally:
        print(f'Сумма чисел: {r}')
