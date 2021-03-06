# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться
# после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# создание списка
my_list = []

# ввод количества элементов списка
n = int(input("Введите количество элементов списка: "))

# наполнение списка
for i in range(n):
    e = int(input(f'Введите целочисленный {i+1}-й элемент списка: '))
    my_list.append(e)
else:
    my_list.sort(reverse=True)
    
# вывод списка
print(f'Начальный список: {my_list}')

# ввод числа
v = -1
while v < 0:
    v = int(input('Введите число: '))
    if v < 0:
        print('Ошибка! Значение должно быть положительным!')
    else:
        if my_list.count(v) != 0:
            my_list.insert(my_list.index(v), v)
        else:
            my_list.append(v)
        my_list.sort(reverse=True)
        break

# вывод списка
print(f'Финальный список: {my_list}')
