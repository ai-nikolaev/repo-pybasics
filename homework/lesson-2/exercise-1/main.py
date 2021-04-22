# создание пустого списка
my_list = []

# ввод количества элементов списка
n = int(input("Введите количество элементов списка: "))

# наполнение списка
for i in range(n):
    value = input(f'Введите {i+1}-й элемент списка: ')
    if value == 'None':
        value = None
    elif value.isnumeric():
        value = int(value)
    else:
        try:
            value = float(value)
        except ValueError:
            pass
    my_list.append(value)

# вывод списка
print(f'Список элементов: {my_list}')

# разбор типов
for e in my_list:
    if isinstance(e, int):
        print(f'Тип данных элемента "{e}" - "int"')
    elif isinstance(e, float):
        print(f'Тип данных элемента "{e}" - "float"')
    elif isinstance(e, str):
        print(f'Тип данных элемента "{e}" - "str"')
    else:
        print(f'Тип данных элемента "{e}" - "{type(e)}"')
