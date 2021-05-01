from sys import argv
from itertools import cycle


# итератор, повторяющий элементы некоторого списка, определенного заранее
def my_cycle_func(array):
    my_list = []
    c = 0
    for el in cycle(array):
        if c > 2 * len(array):
            break
        my_list.append(el)
        c += 1
    return my_list


def my_cycle_show_func(array):
    print(array)


try:
    script_name = argv[0]
    script_params = argv[1:]
    if len(script_params) == 0:
        raise IndexError('Ошибка! Количество параметров равно 0!')
except IndexError:
    pass
else:
    print("Имя скрипта:", script_name)
    print("Параметры скрипта:", script_params)
    try:
        script_params = [int(a) for a in script_params]
    except ValueError:
        print(f'Ошибка! Значение элементов "{script_params}" должно быть целочисленным!')
    else:
        my_cycle_show_func(my_cycle_func(script_params))
