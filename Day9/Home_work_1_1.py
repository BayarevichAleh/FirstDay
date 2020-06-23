"""
1. Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""


class Printer:
    def __init__(self, color_inc_level=100, black_inc_level=100, sheets=0):
        self._color_inc_level = color_inc_level
        self._black_inc_level = black_inc_level
        self._sheets = sheets

    def set_color_inc_level(self, level):
        self._color_inc_level = level

    def get_color_inc_level(self):
        return int(self._color_inc_level)

    def set_black_inc_level(self, level):
        self._black_inc_level = level

    def get_black_inc_level(self):
        return int(self._black_inc_level)

    def set_sheets(self, quantity):
        self._sheets = quantity

    def get_sheets(self):
        return self._sheets

    def print_color_page(self, quantity):
        print("--Выполняется цветная печать--\n")
        if quantity > self._sheets:
            self._color_inc_level -= self._sheets / 10
            self._sheets = 0
            print("Печать прервана (В лотке нет бумаги)\n")
        else:
            self._color_inc_level -= quantity / 10
            self._sheets -= quantity

    def print_black_page(self, quantity):
        print("--выполняется черно-белая печать--\n")
        if quantity > self._sheets:
            self._black_inc_level -= self._sheets / 10
            self._sheets = 0
            print("Печать прервана (В лотке нет бумаги)\n")
        else:
            self._black_inc_level -= quantity / 10
            self._sheets -= quantity


a = lambda: f"Цветной картридж: {my_printer.get_color_inc_level()} %\nЧерный картридж: {my_printer.get_black_inc_level()} %\nОсталось страниц: {my_printer.get_sheets()}\n"

my_printer = Printer(sheets=50)
print(a())
my_printer.print_color_page(15)
print(a())
my_printer.print_black_page(21)
print(a())
my_printer.print_black_page(15)
print(a())
my_printer.set_sheets(100)
print(a())
my_printer.print_color_page(15)
print(a())
