"""
2. Создать класс Car.
Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости).
Все атрибуты приватные.
"""

class Car():
    def __init__(self, make, mark, year, speed = 0):
        self._make = make
        self._mark = mark
        self._year = year
        self._speed = speed

    def speed_up(self):
            self._speed += 5

    def speed_down(self):
            self._speed -= 5

    def stop(self):
        self._speed = 0

    def view_speed(self):
        print(self._speed)

    def turn(self):
        self._speed *= -1


my_car = Car("Lada","Kalina",2018)

my_car.view_speed()
my_car.speed_up()
my_car.speed_up()
my_car.speed_up()
my_car.view_speed()
my_car.turn()
my_car.view_speed()
my_car.speed_down()
my_car.view_speed()



