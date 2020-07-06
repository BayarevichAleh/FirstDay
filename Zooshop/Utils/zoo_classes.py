class Animal:
    """
    Класс создания животного
    """
    import re

    def __init__(self, animal, name, gender, cost, any_args=''):
        """
        :param animal: Тип животного (собака, кошка, хомяк и т.д.)
        :param name: Имя животного (Тузик, Бобик, Мурка и т.д.)
        :param gender: Пол животного
        :param cost: Стоимость данного животного
        :param any_args: Произвольные аргументы (формат вводимых данных строка типа "arg_1=value_1 arg_2=value_2, arg_3=value_3 и т.д.")
        """
        self.animal = animal
        self.name = name
        self.gender = gender
        self.cost = cost
        self.any_args = dict(self.re.findall('(\w+)=(\w+)', any_args))
        for i in self.any_args:
            try:
                self.any_args[i] = float(self.any_args[i])
            except:
                pass

    @property
    def get_info(self):
        """
        Получение полной информации о животном
        :return: dict
        """
        return_dict = {'Animal': self.animal, 'Name': self.name, 'Gender': self.gender, 'Cost': self.cost, }
        return_dict.update(self.any_args)
        return return_dict

    def set_args(self, animal=None, name=None, gender=None, cost=None, any_args=''):
        """
        Обновление или добавление параметров животного
        :param animal:
        :param name:
        :param gender:
        :param cost:
        :param kwargs:
        :return:
        """
        self.animal = animal if animal != None else self.animal
        self.name = name if name != None else self.name
        self.gender = gender if gender != None else self.gender
        self.cost = cost if cost != None else self.cost
        self.any_args.update(dict(self.re.findall('(\w+)=(\w+)', any_args))) if any_args != '' else self.any_args
        for i in self.any_args:
            try:
                self.any_args[i] = float(self.any_args[i])
            except:
                pass

    def __del__(self):
        print(f"Животное {self.get_info} удалено")


class zooshop:
    """
    Класс зоомагазина
    :param money: доход магазина
    """
    import json
    import re
    __money = 0

    def __init__(self):
        """
        :param quantity_animals: Счетчик созданых жифотных
        :param animals: Словарь животных
        """
        self.quantity_animals = 0
        self.animals = {}

    def add_animal(self, animal):
        """
        Добавление нового животного в базу
        :param animal: экземпляр класса Animal
        :return:
        """
        if type(animal) == Animal:
            self.animals[self.quantity_animals] = animal
            self.quantity_animals += 1

    @property
    def list_categories(self):
        """
        Вывод списка категорий животных, в скобках выводится количество животных в данной категории
        :return:
        """
        list_categories = {}
        for i in self.animals:
            if self.animals[i].get_info['Animal'] not in list_categories:
                list_categories[self.animals[i].get_info['Animal']] = 1
            else:
                list_categories[self.animals[i].get_info['Animal']] += 1
        for i in list_categories:
            print(f"{i} - {list_categories[i]} animal(s)")
        if list_categories == {}:
            print("In shop no annimals")
        # for i in self.animals_data:
        #     print(f"{i}({self.animals_data[i]['Quentity']})")

    def list_animals(self, category=None):
        """
        Вывод списка животных указанной категории в формате: id:(0,1,2,....) - {все параметры животного}
        Если категория не указана то вывводится список всех животных в базе
        :param category: Категория животных ("Dog", "Cat", "Rabbit")
        :return:
        """
        if category == None:
            for i in self.animals:
                print(f"id:{i} - {self.animals[i].get_info}")
            if self.animals == {}:
                print("In shop no annimals")
        else:
            find = False
            for i in self.animals:
                if self.animals[i].get_info["Animal"] == category:
                    find = True
                    print(f"id:{i} - {self.animals[i].get_info}")
            if find == False:
                print(f'No category "{category}"')

    def buy_animal(self, id):
        """
        Покупка животного
        :param id: id животного
        :return:
        """
        try:
            zooshop.__money += self.animals[id].get_info['Cost']
            #self.quantity_animals -= 1
            print(f"You have bought {self.animals[id].get_info['Animal']}")
            del self.animals[id]
        except:
            print(f"No id:{id}")

    def update_animal(self, id, animal=None, name=None, gender=None, cost=None, any_args=None):
        try:
            self.animals[id].set_args(animal, name, gender, cost, any_args)
        except:
            print(f"No id:{id}")

    @property
    def get_money(self):
        """
        Просмотр количества заработанных денег
        :return:
        """
        return self.__money

    def save(self):
        """
        Сохранение данных в json-файл
        :return:
        """
        with open('zooshop.json', 'w') as my_file:
            save_animals = {"Money": self.__money, "Quantity": self.quantity_animals}
            for i in self.animals:
                try:
                    save_animals["Animals"][i] = self.animals[i].get_info
                except:
                    save_animals["Animals"] = {i: self.animals[i].get_info}
            my_file.write(self.json.dumps(save_animals, indent=4))

    def load(self):
        """
        Извлечение данных из json-файла.
        Если животное с id из файла уще существует, его параметры обновятся данными из файла
        :return:
        """
        with open('zooshop.json', 'r') as my_file:
            a = self.json.loads(my_file.read())
            self.__money = a["Money"]
            any_args = ''
            for i in a["Animals"]:
                for j in a["Animals"][i]:
                    if j == 'Animal':
                        animal = a["Animals"][i][j]
                    elif j == 'Name':
                        name = a["Animals"][i][j]
                    elif j == 'Gender':
                        gender = a["Animals"][i][j]
                    elif j == 'Cost':
                        cost = float(a["Animals"][i][j])
                    elif self.re.match(r'\w+=\w+$', i):
                        try:
                            parametr = float(self.re.findall(r'\w+=\w+$', i)[0])
                        except:
                            parametr = self.re.findall(r'\w+=\w+$', i)[0].title()
                        any_args = f"{any_args} {parametr}"
                if int(i) in self.animals:
                    self.update_animal(int(i), animal, name, gender, cost, any_args)
                else:
                    self.add_animal(Animal(animal, name, gender, cost, any_args))

    def del_animal(self, id):
        """
        Удаление животного
        :param id: id животного
        :return:
        """
        try:
            del self.animals[id]
            #self.quantity_animals -= 1
            print(f"Animal {id} was deleted")
        except:
            print(f"No id:{id}")

