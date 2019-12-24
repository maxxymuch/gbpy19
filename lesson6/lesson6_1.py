#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time

class Colors:
    YELLOW = '\033[93m'
    STOP = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

class TrafficLight():
    #__color = "color"

    def traffic_timer(self, start):
        for a in range(start, 0, -1):
            print(a)
            time.sleep(1)

    def running(self, color):
        self.color = color
        if self.color == "red":
            print(Colors.STOP, "STOP", Colors.END)
            self.traffic_timer(7)
        elif self.color == "yellow":
            print(Colors.YELLOW, "STADY", Colors.END)
            self.traffic_timer(2)
        elif self.color == "green":
            print(Colors.GREEN, "GO", Colors.END)
            self.traffic_timer(9)
        else:
            print("TrafficLight is broken")

###################################    main    #########################

traffic_lights = ["red", "yellow", "green", "yellow"]
tr = TrafficLight()

while True:
    for light in traffic_lights:
        tr.running(light)