"""
1. Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
"""

import csv_utils

fields = ["Имя", "Фамилия", "Возраст"]
data = [
    ["Олег", "Бояревич", 33],
    ["Игорь", "Петров", 57],
    ["Алеся", "Иванова", 13],
    ["Светлана", "Сидорова", 17],
    ["Андрей", "Андреев", 24],
    ["Кирилл", "Кириллов", 2],
]

csv_utils.csv_write('data.csv', fields, data)
data = csv_utils.csv_read('data.csv')
categories = {"1-12": 0, "13-18": 0, "19-25": 0, "26-40": 0, "40+": 0}
for i in range(1, len(data)):
    age = int(data[i][2])
    if age > 0 and age < 13:
        categories["1-12"] += 1
    elif age > 12 and age < 19:
        categories["13-18"] += 1
    elif age > 18 and age < 26:
        categories["19-25"] += 1
    elif age > 25 and age < 41:
        categories["26-40"] += 1
    else:
        categories["40+"] += 1

print(categories)

csv_utils.csv_write('categories.csv', list(categories.keys()), [list(categories.values())])
