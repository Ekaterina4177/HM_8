import csv


def add_information(sur, name, ph_num, com):  # была выполнена первая запись
    with open('database.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fnames = ['id', 'Surname', 'Name', 'Phone number', 'Comment']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fnames)

        csv_writer.writeheader()
        for i in range(1, 2):
            csv_writer.writerow({'id': f"{i}", 'Surname': f"{sur}", 'Name': f"{name}",
                                'Phone number': f"{ph_num}", 'Comment': f"{com}"})


def read_information_id():  # для поиска максимального id
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:
            if max_id < int(row['id']):
                max_id = int(row['id'])
        return max_id


# удаление информации переносом в файл "datebasecopy.csv"
def read_information_id_dell(id):
    with open("database.csv", 'r', encoding='utf8', newline='') as source, open("datebasecopy.csv", "w", encoding='utf8', newline='') as dest:
        reader = csv.reader(source, delimiter=',')
        writer = csv.writer(dest, delimiter=',')
        skip_lines = [id+1]
        for line, row in enumerate(reader, 1):
            if line in skip_lines:
                continue
            writer.writerow(row[0:])


def read_information_id_search(id):  # поиск по id
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if id == int(row['id']):
                print('Информация по абоненту:', 'id:', row['id'], 'Surname:', row['Surname'], 'Name:',
                      row['Name'], 'Phone number:', row['Phone number'], 'Comment:', row['Comment'])
                id = row['id']
                sur = row['Surname']
                name = row['Name']
                num = row['Phone number']
                com = row['Comment']
                a = id + ' ' + sur + ' ' + name + ' ' + num + ' ' + com
                return a


def read_information_surname(num):  # поиск по номеру
    with open('database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        search_number = num
        for row in reader:
            if search_number == row['Phone number']:
                print('Информация по абоненту:', 'id:', row['id'], 'Surname:', row['Surname'], 'Name:',
                      row['Name'], 'Phone number:', row['Phone number'], 'Comment:', row['Comment'])
                id = row['id']
                sur = row['Surname']
                name = row['Name']
                num = row['Phone number']
                com = row['Comment']
                a = id + ' ' + sur + ' ' + name + ' ' + num + ' ' + com
                return a


def write_info(max, sur, name, ph_num, com):  # перезапись с id на повышение
    with open('database.csv', 'a', encoding='utf-8') as csvfile:
        field_names = ['id', 'Surname', 'Name', 'Phone number', 'Comment']
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_writer.writerow({'id': max + 1, 'Surname': f"{sur}", 'Name': f"{name}",
                             'Phone number': f"{ph_num}", 'Comment': f"{com}"})


def dell_information_id_search(id):  # поиск по id
    with open('databasecopy.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if id == int(row['id']):
                print('Информация по абоненту:', 'id:', row['id'], 'Surname:', row['Surname'], 'Name:',
                      row['Name'], 'Phone number:', row['Phone number'], 'Comment:', row['Comment'])
                id = row['id']
                sur = row['Surname']
                name = row['Name']
                num = row['Phone number']
                com = row['Comment']
                a = id + ' ' + sur + ' ' + name + ' ' + num + ' ' + com
                return a
            if id:
                print(
                    'Информация о пользователе не найдена \nПроверьте корректность ввода данных')
                return
