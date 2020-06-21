"""
3. Дан файл, содержащий различные даты.
Каждая дата - это число, месяц и год.
Найти самую раннюю дату.
"""
import json
import datetime

a = ["01-01-1994", "10-04-1847", "07-09-2010", "21-11-2017", "13-04-1847"]

with open('dates.json', 'w') as my_file_1:
    my_file_1.write(json.dumps(a))

with open('dates.json', 'r') as my_file_1:
    read_data = json.loads(my_file_1.read())

get_date = list()
for i in read_data:
    j = i.split('-')
    get_date.append(datetime.date(int(j[2]), int(j[1]), int(j[0])))


min_date = min(get_date)
print(min_date)



