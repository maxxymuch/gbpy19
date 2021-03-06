# 2.Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина ширина масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    CONST_MASS = 25
    CONST_HI = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_calc(self):
        return self._length * self._width * self.CONST_HI * self.CONST_MASS / 1000

############################################### main ###############################################

road = Road(20, 5000)
print(road.road_calc())
