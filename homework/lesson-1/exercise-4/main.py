# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

# ввод данных
user_value = 0
while user_value <= 0:
    user_value = int(input('Введите целое положительное число: '))
    if user_value < 0:
        print('Ошибка! Число должно быть положительным!')
    elif user_value == 0:
        print('Ошибка! Число 0 не является ни положительным, ни отрицательным числом!')
        
# вычисление самой большой цифры
index = 0
max_value = 0
values = str(user_value)
max_index = len(values)
while index != max_index:
    temp_value = int(values[index])
    index += 1
    if temp_value > max_value:
        max_value = temp_value

# вывод
print(f'Самая большая цифра в числе \'{user_value}\' это \'{max_value}\'.')
