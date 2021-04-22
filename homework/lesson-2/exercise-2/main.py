# создание пустого списка
my_list = []

# ввод количества элементов списка
n = int(input("Введите количество элементов списка: "))

# проверка значения
if n < 1:
    raise ValueError('Значение введено неверно! Допустимое значение >= 1.')

# наполнение списка
for i in range(n):
    e = int(input(f'Введите целочисленный {i+1}-й элемент списка: '))
    my_list.append(e)

# вывод списка
print(f'Начальный список: {my_list}')

# выборка по нечетным индексам списка
for i in range(1, len(my_list), 2):
    x, y = my_list[i-1], my_list[i]
    my_list[i-1], my_list[i] = y, x

# вывод списка
print(f'Итоговый список: {my_list}')
