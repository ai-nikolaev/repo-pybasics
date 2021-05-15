# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DivideByZeroException(Exception):
    
    def __init__(self, message):
        self.message = message
        
class MyDivider:
    
    @staticmethod
    def Calculate(divisible, divider):
        if divider == 0:
            raise DivideByZeroException('Деление на ноль.')
        return divisible / divider

divisible = int(input('Введите целое число (делимое): '))
divider = int(input('Введите целое число (делитель): '))

try:
    print(f'Ответ: {MyDivider.Calculate(divisible, divider)}')
except DivideByZeroException as e:
    print(f'Ошибка! {e}')
