# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


# функция вычисления произведения
def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


# формирование списка
my_list = [a for a in range(100, 1001) if a % 2 == 0]

# вывод итоговых данных
print(f'Вывод результата: {reduce(my_func, my_list)}')
