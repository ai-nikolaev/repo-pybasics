# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from random import randint
from enum import Enum

class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

class TrafficLight:
    __color = Color.RED
    
    def running(self):
        while True:
            try:
                self.__color = Color.RED
                print(f'Сейчас горит "{self.__color}" сигнал светофора.')
                sleep(7)  # ждём 7 секунд
                self.__color = Color.YELLOW
                print(f'Сейчас горит "{self.__color}" сигнал светофора.')
                sleep(2)  # ждём 2 секунды
                self.__color = Color.GREEN
                print(f'Сейчас горит "{self.__color}" сигнал светофора.')
                sleep(randint(2, 7))  # ждём несколько секунд
            except KeyboardInterrupt:
                print('Завершение работы светофора.')
                break


my_traffic_light = TrafficLight()
my_traffic_light.running()
