# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    
    def __init__(self, date_as_string):
        self.date_as_string = date_as_string
        
    @classmethod
    def extract_numbers(cls, date):
        return [int(number) for number in date.date_as_string.split('-')]
    
    @staticmethod
    def Validate(day, month, year):
        if day not in [1,31]:
            raise ValueError(f'Ошибка! Некорректное значения дня "{day}".')
        elif month not in [1,12]:
            raise ValueError(f'Ошибка! Некорректное значения месяца "{month}".')
        elif year < 0:
            raise ValueError(f'Ошибка! Некорректное значения года "{year}".')
    
my_date = Date('31-12-2012')
my_date_values = Date.extract_numbers(my_date)
print(my_date_values)
print(Date.Validate(my_date_values[0], my_date_values[1], my_date_values[2]))
