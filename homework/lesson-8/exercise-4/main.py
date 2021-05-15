# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

class Sklad:
    
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def register(self, *items):
        self.items.extend(list(items))

class Orgtehnika:
    
    def __init__(self, brand, color):
        self.Brand = brand
        self.Color = color
        
    def __str__(self):
        return f"Brand and Color: {self.Brand} {self.Color}"

class Printer(Orgtehnika):
    
    def __init__(self, brand, color):
        super().__init__(brand, color)
    
class Skaner(Orgtehnika):
    
    def __init__(self, brand, color):
        super().__init__(brand, color)
    
class Kserox(Orgtehnika):
    
    def __init__(self, brand, color):
        super().__init__(brand, color)
        
my_item1 = Printer('Эпл', 'Белый')
print(my_item1)
my_item2 = Skaner('ЭйчПи', 'Чёрный')
print(my_item2)
my_item3 = Kserox('Майкрософт', 'Чёрный')
print(my_item3)

my_sklad = Sklad('Рога и Копыта')
print(my_sklad.name)

my_sklad.register(my_item1)
my_sklad.register(my_item2)
my_sklad.register(my_item3)

print(my_sklad.items[0])
