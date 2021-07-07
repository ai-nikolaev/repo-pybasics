# 2. Реализовать проект расчета суммарного расхода ткани на
# производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая
# может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных
# данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABCMeta, abstractmethod

class Сlothes(metaclass=ABCMeta):
    
    @abstractmethod
    def FabricConsumption(self):
        raise NotImplmentedError

class Coat(Сlothes):
    
    def __init__(self, size):
        self.__size = size
    
    @property
    def FabricConsumption(self):
        return (self.__size/6.5 + 0.5)
    
class Suit(Сlothes):
    
    def __init__(self, height):
        self.__height = height
        
    @property
    def FabricConsumption(self):
        return (2 * self.__height + 0.3)

print(Coat(3).FabricConsumption)
print(Suit(3).FabricConsumption)
