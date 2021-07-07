# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа
# и строки. При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

class NotOnlyNumbersException(Exception):
    
    def __init__(self, message):
        self.message = message
    
    @classmethod
    def are_numerics(cls, values):
        return all([str(a).isnumeric() for a in values])

print(NotOnlyNumbersException.are_numerics([1, 2, 3]))
print(NotOnlyNumbersException.are_numerics([1, '2', 3]))
print(NotOnlyNumbersException.are_numerics([1, 'b', 3]))

my_list = []

while True:
    value = input('Введите значение: ')
    if value == 'stop':
        print(f'Список: "{my_list}".')
        break
    else:
        try:
            if NotOnlyNumbersException.are_numerics(value):
                my_list.append(value)
            else:
                raise NotOnlyNumbersException('Введенное значение элемента не является цифренным.')
        except NotOnlyNumbersException as e:
            print(e)
