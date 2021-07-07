# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Пишу текст с помощью ручки "{self.title}".')


class Pencil(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Рисую чертеж с помощью карандаша "{self.title}".')


class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Делаю заметки с помощью маркера "{self.title}".')


my_item1 = Pen('Лучшая ручка')
my_item2 = Pencil('Великолепный карандаш')
my_item3 = Handle('Самый лучший маркер')

print(my_item1.title)
print(my_item2.title)
print(my_item3.title)

my_item1.draw()
my_item2.draw()
my_item3.draw()
