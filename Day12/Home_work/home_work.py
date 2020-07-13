"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс.
"""

from UI import *


my_base = database('study','study','study')
print("Enter 'help' to view commad")
while True:
    UI(my_base)