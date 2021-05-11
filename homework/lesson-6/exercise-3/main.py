# 3. Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров).

class Worker:  
    
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = {"wage": 0, "bonus": 0}
        
class Position(Worker):
    
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
    
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    
    def get_total_income(self):
        return sum(self._income.values())

# сотрудники
my_worker_1 = Position('Александр', 'Пушкин', 'писатель', {"wage": 35000, "bonus": 50000})
my_worker_2 = Position('Василий', 'Пупкин', 'инженер', {"wage": 55000, "bonus": 75000})

# вывод информации о сотруднике
print(my_worker_1.name)
print(my_worker_1.surname)
print(my_worker_1.position)
print(my_worker_1.get_full_name())
print(my_worker_1.get_total_income())

# вывод информации о сотруднике
print(my_worker_2.name)
print(my_worker_2.surname)
print(my_worker_2.position)
print(my_worker_2.get_full_name())
print(my_worker_2.get_total_income())
