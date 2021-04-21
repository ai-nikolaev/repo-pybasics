user_value = 0
while user_value <= 0:
    user_value = int(input('Введите целое положительное число: '))
    if user_value < 0:
        print('Неверно! Число должно быть положительным!')
    elif user_value == 0:
        print('Неверно! Число 0 не является ни положительным, ни отрицательным числом!')
values = list(str(user_value))
max_value = 0
while len(values) != 0:
    temp_value = int(values.pop(0))
    if temp_value > max_value:
        max_value = temp_value
print(f'Самая большая цифра в числе \'{user_value}\' это \'{max_value}\'.')
