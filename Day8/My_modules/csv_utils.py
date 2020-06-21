import csv


def csv_read(file_name):
    """
    Функция чтения CSV
    :param file_name: Имя файли CSV
    :return: Содержимое файла CSV в виде списка
    """
    rows = []
    with open(file_name, 'r') as my_file:
        csvreader = csv.reader(my_file)
        for row in csvreader:
            rows.append(row)
    return rows


def csv_write(file_name, fields, data):
    """
    Функция записи/создания CSV файла
    :param file_name: Имя файли CSV
    :param fields: Названия колонок
    :param data: Содержимое строк
    """
    with open(file_name, 'w', newline='') as my_file:
        csvwriter = csv.writer(my_file)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)


def csv_add(file_name, data, position=0):
    """
    Функция добавления записи в файл CSV
    :param file_name: Имя файли CSV
    :param data: Содержимое строки
    :param position: Номер строки куда необходимо вставить данные (0 - добавляет в конец файла)
    """
    with open(file_name, 'r+', newline='') as my_file:
        rows = []
        csvreader = list(csv.reader(my_file))
        if position == 0:
            csvreader.append(data)
        else:
            csvreader.insert(position,data)
        # for line in csvreader:
        #     if csvreader.line_num - 1 == position and position != 0:
        #         rows.append(data)
        #     rows.append(line)
        # if position == 0:
        #     rows.append(data)
        my_file.seek(0)
        csvwriter = csv.writer(my_file)
        csvwriter.writerows(rows)


def csv_remove(file_name, position=0):
    """
    Фнкция удаления записи в файле CSV
    :param file_name: Имя файли CSV
    :param position: Номер строки подлежащей удалению (0 - Удаляет последнюю строку)
    """
    with open(file_name, 'r+', newline='') as my_file:
        rows = []
        csvreader = csv.reader(my_file)
        for line in csvreader:
            if csvreader.line_num - 1 != position or position == 0:
                rows.append(line)
        if position == 0:
            rows.pop()
        my_file.seek(0)
        csvwriter = csv.writer(my_file)
        csvwriter.writerows(rows)
        my_file.truncate()


def sum_cost_all(file_name):
    """
    Функция подсчета суммы всех товаров
    :param file_name: Имя файли CSV
    :return: Сумма всех товаров
    :type return: int
    """
    data = csv_read(file_name)
    sum = 0
    for i in range(1, len(data)):
        sum += int(data[i][1]) * int(data[i][2])
    return sum


def the_biggest_cost(file_name):
    """
    Функция нахождения товара с максимальной стоимостью
    :param file_name: Имя файли CSV
    :return: Возвражает список товаров с самой высокой ценой
    """
    data = csv_read(file_name)
    max = list()
    max.append(data[1])
    for i in range(2, len(data)):
        cost = int(data[i][1])
        if int(max[0][1]) < cost:
            max = []
            max.append(data[i])
        elif int(max[0][1]) == cost:
            max.append(data[i])
    return max


def the_least_cost(file_name):
    """
    Функция нахождения товара с наименьшей стоимостью
    :param file_name: Имя файли CSV
    :return: Возвражает список товаров с самой низкой ценой
    """
    data = csv_read(file_name)
    min = list()
    min.append(data[1])
    for i in range(2, len(data)):
        cost = int(data[i][1])
        if int(min[0][1]) > cost:
            min = []
            min.append(data[i])
        elif int(min[0][1]) == cost:
            min.append(data[i])
    return min


def amout_down(file_name, position, num=1):
    data = csv_read(file_name)
    a = int(data[position][2])
    a -= num
    data[position][2] = a
    fields = data.pop(0)
    csv_write(file_name, fields, data)
    return f"Количество {data[position-1][0]} уменьшилось на {num}"
