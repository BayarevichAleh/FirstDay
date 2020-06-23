"""
1. Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""


class Phone_book:
    def __init__(self, memory=100):
        self._contacts = {0: {"name": "number"}}
        self._last_contact = 0
        self._memory = [0, memory]

    def set_contact(self, name, number):
        id = list(self._contacts.keys())
        if self._memory[0] < self._memory[1]:
            for i in range(len(id) + 1):
                if i not in id:
                    self._contacts[i] = {name: number}
                    self._memory[0] += 1
                    print(f"Контакт {name} добавлен")
        else:
            print(f"Контакт {name} не добавлен (Недостаточно памяти)")

    def get_contact(self, name):
        for i in self._contacts:
            if list(self._contacts[i].keys())[0] == name:
                return self._contacts[i]
        return f"Контакт {name} не найден"

    def get_contacts(self):
        return self._contacts

    def remove_contact(self, name):
        j = None
        for i in self._contacts:
            if list(self._contacts[i].keys())[0] == name:
                j=i
                break
        if j != None:
            self._contacts.pop(j)
            self._memory[0] -= 1
            print(f"Контакт {name} удален")
        else:
            print(f"Контакт {name} не найден")

    def view_memory(self):
        print(f"Память: {self._memory[0]} из {self._memory[1]}")


my_phone_book = Phone_book(5)
my_phone_book.set_contact("Aleh", "+375257789166")
my_phone_book.set_contact("Max", "+375297542166")
my_phone_book.set_contact("Alex", "+375446584177")
my_phone_book.view_memory()
print(my_phone_book.get_contact("Max2"))
print(f"Все контакты:\n{my_phone_book.get_contacts()}")
my_phone_book.remove_contact("Max2")
my_phone_book.remove_contact("Max")
print(f"Все контакты:\n{my_phone_book.get_contacts()}")
my_phone_book.view_memory()
my_phone_book.set_contact("Maxim", "+375297542166")
my_phone_book.set_contact("Sasha", "+375297542166")
my_phone_book.set_contact("Olya", "+375297542166")
my_phone_book.set_contact("Kate", "+375297542166")

#------------------------------------------------------------------------------------------------------

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
