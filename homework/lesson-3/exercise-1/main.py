# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

# реализация функция
def my_func(p_1, p_2):
    """
    Возвращает частное от деления.

    Именованные параметры:
    p_1 -- делимое
    p_2 -- делитель

    (number, number) -> number

    >>> my_func(10, 10)
    1
    """
    return p_1 / p_2


# ввод делимого
v1 = int(input('Введите число (делимое): '))

# ввод делителя
while True:
    v2 = int(input('Введите число (делитель): '))
    if v2 == 0:
        print(f'Ошибка! Деление на ноль!')
    else:
        break

# вывод результата
print(f'Результат вызова функции: {my_func(v1, v2)}')
