# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# исходные данные
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вывод исходных данных
print(f"Исходный список: {my_list}")

# новые данные
my_new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i-1] < my_list[i]]

# вывод итоговых данных
print(f"Новый список: {my_new_list}")