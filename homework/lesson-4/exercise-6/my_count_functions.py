from sys import argv
from itertools import count

def my_count_func(number):
    my_list = []
    for el in count(number):
        if el > number + 7:
            break
        else:
            my_list.append(el)
    return my_list

def my_count_show_func(array):
    print(array)

try:
    script_name = argv[0]
    script_param = argv[1]
except IndexError:
    pass
else:
    print("Имя скрипта:", script_name)
    print("Параметр скрипта:", script_param)
    try:
        int(script_param)
    except ValueError:
        print(f'Значение "{script_param}" должно быть целочисленным!')
    else:
        my_count_show_func(my_count_func(int(script_param)))
