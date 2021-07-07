# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.

class Sklad:
    
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def register(self, *items):
        self.items.extend(items)

class Orgtehnika:
    
    def __init__(self, brand, color):
        self.Brand = brand
        self.Color = color
        
    def __str__(self):
        return f"Brand and Color: {self.Brand} {self.Color}"

class Printer(Orgtehnika):
    
    def __init__(self, brand, color, type):
        super().__init__(brand, color)
        self.type = type
    
class Skaner(Orgtehnika):
    
    def __init__(self, brand, color, size):
        super().__init__(brand, color)
        self.size = size
    
class Kserox(Orgtehnika):
    
    def __init__(self, brand, color, is_professional):
        super().__init__(brand, color)
        self.is_professional = is_professional
        
my_item1 = Printer('Эпл', 'Белый', 'лазерный')
print(my_item1)
my_item2 = Skaner('ЭйчПи', 'Чёрный', 'А4')
print(my_item2)
my_item3 = Kserox('Майкрософт', 'Чёрный', True)
print(my_item3)

my_sklad = Sklad('Рога и Копыта')
print(my_sklad.name)

my_sklad.register(my_item1, my_item2, my_item3);
print(my_sklad.items)
