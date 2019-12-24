# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки on Main")

class Pen(Stationery):
    def draw(self):
        print(f"Рисуем ручкой с именем {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисует {self.title} карандаш")

class Handle(Stationery):
    def draw(self):
        print(f"Рисует {self.title} маркер")


############################################### main ###############################################

stationery = Stationery("ABC Class")
stationery.draw()

pen = Pen("Parker")
pen.draw()

pencil = Pencil("серый")
pencil.draw()

handle = Handle("красный")
handle.draw()