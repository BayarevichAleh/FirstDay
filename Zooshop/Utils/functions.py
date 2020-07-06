from zoo_classes import *
import re


def Create_animal():
    """
    Интерфейс создания животного
    :return: экземпляр класса Animal
    """
    animal = input("Enter animal type: ").title()
    name = input("Enter animal name: ").title()
    gender = input("Enter animal gender: ").title()
    try:
        cost = float(input("Enter animal cost: "))
    except:
        print("Error! Incorrect cost")
        return None
    any_args = input("Enter any arguments (format: arg1=value arg2=value, arg3=value): ").title()
    return Animal(animal, name, gender, cost, any_args)


def Update_animal():
    """
    Интерфейс обноввления или добавления парамеров животного
    :return: кортедж параметров
    """
    args = input("Enter parametrs (format: arg1=value arg2=value, arg3=value): ")
    args = re.split(r'[ ,;]', args)
    animal = None
    name = None
    gender = None
    cost = None
    any_args = ''
    for i in args:
        argument = re.findall(r'^\w+=', i)
        argument.append('')
        if argument[0].title() == 'Animal=':
            animal = re.findall(r'\w+$', i)[0].title()
        elif argument[0].title() == 'Name=':
            name = re.findall(r'\w+$', i)[0].title()
        elif argument[0].title() == 'Gender=':
            gender = re.findall(r'\w+$', i)[0].title()
        elif argument[0].title() == 'Cost=':
            try:
                cost = float(re.findall(r'\w+$', i)[0])
            except:
                pass
        elif re.match(r'\w+=\w+$', i):
            argument=re.findall(r'^\w+', i)[0].title()
            try:
                parameter = float(re.findall(r'\w+$', i)[0])
            except:
                parameter = re.findall(r'\w+$', i)[0].title()
            any_args = f"{any_args} {argument}={parameter}"

    return (animal, name, gender, cost, any_args)

