"""
1. Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""


class Phone_book:
    def __init__(self, memory=100):
        self._contacts = {}
        self._last_contact = 0
        self._memory = [0, memory]

    def set_contact(self, name, number):
        id = list(self._contacts.keys())
        if self._memory[0] < self._memory[1]:
            for i in range(len(id)+1):
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
print(my_phone_book.get_contact("Alex2"))
print(my_phone_book.get_contact("Alex"))
print(f"Все контакты:\n{my_phone_book.get_contacts()}")
my_phone_book.remove_contact("Max2")
my_phone_book.remove_contact("Max")
print(f"Все контакты:\n{my_phone_book.get_contacts()}")
my_phone_book.view_memory()
my_phone_book.set_contact("Maxim", "+375297542166")
my_phone_book.set_contact("Sasha", "+375297542166")
my_phone_book.set_contact("Olya", "+375297542166")
my_phone_book.view_memory()
my_phone_book.set_contact("Kate", "+375297542166")
my_phone_book.view_memory()
print(f"Все контакты:\n{my_phone_book.get_contacts()}")