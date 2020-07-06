from zoo_classes import *
from functions import *
import re


my_zooshop = zooshop()

print('Enter "help" to view instruction')

while True:
    actions = input("Enter action: ")
    if actions == 'help' or actions == 'Help':
        print("add - add animal")
        print("categories - view categories")
        print("animals - view all animals")
        print("animals {categories} - view animals in selected category")
        print("buy {id} - buy animal with selected id")
        print("money - view earnings of shop")
        print("update {id} - update parameters of animal with selected id")
        print("load - load animals from file")
        print("save - save animals to file")
        print("del {id} - delete animal with selected id")
    elif actions == 'add' or actions == 'Add':
        my_zooshop.add_animal(Create_animal())
    elif actions == 'categories' or actions == 'Categories':
        my_zooshop.list_categories
    elif actions == 'animals' or actions == 'Animals':
        my_zooshop.list_animals()
    elif re.match(r'animals \w+$', actions) or re.match(r'Animals \w+$', actions):
        my_zooshop.list_animals(re.findall(r'\w+$', actions)[0].title())
    elif re.match(r'buy \d+$', actions) or re.match(r'Buy \d+$', actions):
        my_zooshop.buy_animal(int(re.findall(r'\d+$', actions)[0]))
    elif actions == 'money' or actions == "Money":
        print(my_zooshop.get_money)
    elif re.match(r'update \d+$', actions) or re.match(r'Update \d+$', actions):
        args = Update_animal()
        my_zooshop.update_animal(int(re.findall(r'\d+$', actions)[0]), args[0], args[1], args[2], args[3], args[4])
    elif actions == 'save' or actions == 'Save':
        my_zooshop.save()
    elif actions == 'load' or actions == 'Load':
        my_zooshop.load()
    elif re.match(r'del \d+$', actions) or re.match(r'Del \d+$', actions):
        my_zooshop.del_animal(int(re.findall(r'\d+$', actions)[0]))
    else:
        print("Unknow command!")

# my_zoo.add_animal(wolf)
# my_zoo.add_animal(dog)
