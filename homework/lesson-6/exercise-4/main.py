# 4. Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint

class Car:  
    speed = 0
    color = ''
    name = ''
    is_police = False
        
    def go(self):
        self.speed += randint(25, 90)
        print(f'Автомобиль "{self.name}" движется.')
    
    def stop(self):
        self.speed = 0
        print(f'Автомобиль "{self.name}" остановился.')
    
    def turn(self):
        delta = randint(3, 7)
        if (self.speed - delta) > 0:
            self.speed -= delta
        print(f'Автомобиль "{self.name}" выполнил поворот.')
    
    def show_speed(self):
        print(f'Скорость автомобиля "{self.name}" - "{self.speed}" км/ч.')
    
class TownCar(Car):
    
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.speed_limit = 60
    
    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Автомобиль "{self.name}" превысил скоростной лимит "{self.speed_limit}"!')

class SportCar(Car):
    
    def __init__(self, name, color):
        self.color = color
        self.name = name

class WorkCar(Car):
    
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.speed_limit = 40
    
    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Автомобиль "{self.name}" превысил скоростной лимит "{self.speed_limit}"!')

class PoliceCar(Car):
    
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = True

my_car1 = TownCar('A', 'white');
my_car2 = SportCar('B', 'black');
my_car3 = WorkCar('C', 'white');
my_car4 = PoliceCar('D', 'black');

my_car1.go();
my_car2.go();
my_car3.go();
my_car4.go();

my_car1.stop();
my_car2.turn();
my_car3.stop();
my_car4.turn();

my_car1.go();
my_car2.turn();
my_car3.go();
my_car4.turn();

my_car1.show_speed();
my_car2.show_speed();
my_car3.show_speed();
my_car4.show_speed();

print(f'{my_car1.name} {my_car1.color} {my_car1.speed} {my_car1.is_police}')
print(f'{my_car2.name} {my_car2.color} {my_car2.speed} {my_car2.is_police}')
print(f'{my_car3.name} {my_car3.color} {my_car3.speed} {my_car3.is_police}')
print(f'{my_car4.name} {my_car4.color} {my_car4.speed} {my_car4.is_police}')
