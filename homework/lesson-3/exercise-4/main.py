# 4. Программа принимает действительное положительное число x
# и целое отрицательное число y. Выполните возведение числа x
# в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

# реализация функции через оператор **
def my_func_1(x, y):
    """
    Возвращает возведение числа x в степень y.

    Именованные параметры:
    x -- число
    y -- степень

    (number, number) -> number

    >>> my_func_1(2, 2)
    4
    """
    return x ** y


# реализация функции через функцию pow()
def my_func_2(x, y):
    """
    Возвращает возведение числа x в степень y.

    Именованные параметры:
    x -- число
    y -- степень

    (number, number) -> number

    >>> my_func_2(2, 2)
    4
    """
    return pow(x, y)


# реализация функции через пользовательское возведение в степень
def my_func_3(x, y):
    """
    Возвращает возведение числа x в степень y.

    Именованные параметры:
    x -- число
    y -- степень

    (number, number) -> number

    >>> my_func_3(2, 2)
    4
    """
    if y < 0:
        r = 1.0
        for _ in range(abs(y)):
            r *= x
        r = 1 / r
        return r
    elif y > 0:
        r = 1
        for _ in range(abs(y)):
            r *= x
        return r
    return 1


# ввод x
X = 0
while True:
    X = int(input('Введите действительное положительное число X: '))
    if X <= 0:
        print('Ошибка! Число должно быть действительное и положительное!')
    else:
        break

# ввод y
Y = 0
while True:
    Y = int(input('Введите целое отрицательное число Y: '))
    if Y >= 0:
        print('Ошибка! Число должно быть целое и отрицательное!')
    else:
        break

# вывод результатов
print(f'Вывод функции my_func_1({X}, {Y}): {my_func_1(X, Y)}')
print(f'Вывод функции my_func_2({X}, {Y}): {my_func_2(X, Y)}')
print(f'Вывод функции my_func_3({X}, {Y}): {my_func_3(X, Y)}')