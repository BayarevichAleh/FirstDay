from my_classes import *
import re


def UI(database):
    command = input("Enter command: ")
    if command == 'help':
        print("add - add new item")
        print("update {id} - update item with {id}")
        print("remove {id} - remove item with {id}")
        print("list - show all table")
    elif command.upper() == 'ADD':
        values = add_item()
        if values != False:
            database.add_item('products', values[0], values[1], values[2], values[3])
    elif re.match(r"update \d+", command):
        try:
            id = int(re.findall(r'update (\d+)', command)[0])
        except:
            print("")
        values = update_item()
        if values != False:
            database.update_item('products', id, values[0], values[1], values[2], values[3])
    elif re.match(r"remove \d+", command):
        id = int(re.findall(r'remove (\d+)', command)[0])
        database.remove_item('products', id)
    elif re.match(r"find \w+ *= *.+", command):
        column = re.findall(r'find (\w+) *=', command)[0].lower()
        value = re.findall(r'find \w+ *= *(.+)', command)[0]
        if column == 'name' or column == 'cost' or column == 'amount' or column == 'commit':
            database.find_item('products', column, value)
        else:
            print(f"Not find column: {column}")
    elif command == 'list':
        database.list_items('products')
    else:
        print("Unknown command!")


def add_item():
    """
    Интерфейс создания животного
    :return: экземпляр класса Animal
    """
    name = input("Enter product name: ")
    cost = input("Enter product cost: ")
    amount = input("Enter product amount: ")
    commit = input("Enter product commit: ")

    try:
        cost = float(cost)
    except:
        print('Error! Incorrect cost!')
        return False
    try:
        amount = float(amount)
    except:
        print('Error! Incorrect amount!')
        return False
    return (name, cost, amount, commit)


def update_item():
    data = input("Enter new data (format: name=value, cost=value, amount=value, commit = value): ")
    data = re.split(r'[,;]', data)
    name = None
    cost = None
    amount = None
    commit = None
    for i in data:
        if re.match(r' *name *=', i):
            name = re.findall(r'name *= *(.+)', i)[0]
        elif re.match(r' *cost *=', i):
            cost = re.findall(r'cost *= *(.+)', i)[0]
            try:
                cost = float(cost)
            except:
                print('Error! Incorrect cost!')
                return False
        elif re.match(r' *amount *=', i):
            amount = re.findall(r'amount *= *(.+)', i)[0]
            try:
                amount = float(amount)
            except:
                print('Error! Incorrect amount!')
                return False
        elif re.match(r' *commit *=', i):
            commit = re.findall(r'commit *= *(.+)', i)[0]
    if name == None and cost == None and amount == None and commit == None:
        print("No correct data!")
        return False
    return (name, cost, amount, commit)

    #     """
#     Интерфейс обноввления или добавления парамеров животного
#     :return: кортедж параметров
#     """
#     args = input("Enter parametrs (format: arg1=value arg2=value, arg3=value): ")
#     args = re.split(r'[ ,;]', args)
#     animal = None
#     name = None
#     gender = None
#     cost = None
#     any_args = ''
#     for i in args:
#         argument = re.findall(r'^\w+=', i)
#         argument.append('')
#         if argument[0].title() == 'Animal=':
#             animal = re.findall(r'\w+$', i)[0].title()
#         elif argument[0].title() == 'Name=':
#             name = re.findall(r'\w+$', i)[0].title()
#         elif argument[0].title() == 'Gender=':
#             gender = re.findall(r'\w+$', i)[0].title()
#         elif argument[0].title() == 'Cost=':
#             try:
#                 cost = float(re.findall(r'\w+$', i)[0])
#             except:
#                 pass
#         elif re.match(r'\w+=\w+$', i):
#             argument=re.findall(r'^\w+', i)[0].title()
#             try:
#                 parameter = float(re.findall(r'\w+$', i)[0])
#             except:
#                 parameter = re.findall(r'\w+$', i)[0].title()
#             any_args = f"{any_args} {argument}={parameter}"
#
#     return (animal, name, gender, cost, any_args)
