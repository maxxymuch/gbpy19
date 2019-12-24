# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        try:
            self.is_police = bool(is_police)
            if self.is_police is True:
                print("Полицейская машина на дороге\n")
        except TypeError:
            print("Значение не булево")
        print(f"{self.name} на дороге")

    def go(self, speed):
        self.speed = speed
        print(f"Передана команда двигаться со скоростью {speed}")

    def stop(self):
        self.speed = 0
        print("Передана команда остановиться")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина двигается {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Снижайте скорость! Ограничение движения в городе 60 км\ч")
        else:
            print(f"Скорость машины в городе {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Снижайте скорость! Ограничение движения {self.name} 40 км\ч")
        else:
            print(f"Скорость техники {self.speed}")


class PoliceCar(Car):

    def make_sound(self, sound=True):
        self.sound = sound
        if self.sound is True:
            print(f"Погоня с включенной сиреной")
        else:
            print("Мигалка с сиреной выключена")


work_car = WorkCar(35, "серый", "трактор")
work_car.show_speed()
work_car.go(41)
work_car.show_speed()
work_car.turn("направо")
work_car.stop()
work_car.show_speed()
print("\n")

town_car = TownCar(55, "белый", "smart")
town_car.show_speed()
town_car.go(62)
town_car.show_speed()
town_car.stop()
town_car.show_speed()
print("\n")

police_car = PoliceCar(55, "синий", "БМВ", True)
police_car.make_sound()
police_car.go(77)
police_car.turn("прямо")
