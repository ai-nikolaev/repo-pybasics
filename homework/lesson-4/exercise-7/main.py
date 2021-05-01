# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная
# с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from random import randint


# реализация генератора с помощью функции с ключевым словом yield
def fact(n):
    for e in range(1, n + 1):
        yield e


# создание объект-генератора
g = fact(randint(1, 100))

# вывод объект-генератора
print(g)

# вывод первых n чисел с помощью функции
print('Вывод результата:', end=' ')
for el in fact(randint(1, 100)):
    print(el, end=' ')
