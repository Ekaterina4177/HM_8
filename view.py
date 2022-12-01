import sys


def get_menu_start():  # Первоначальное меню
    while True:
        menu_start = input(
            'Выберите операцию: \n1. Добавить нового абонента \n2. Удалить данные абонента \n3. Поиск абонента \n0. Завершить \n>')
        if menu_start == '1':
            return 1
        if menu_start == '2':
            return 2
        if menu_start == '3':
            return 3
        if menu_start == '0':
            return 0
        else:
            print('Вы ввели неккоректное значение типа операции. Повторите ввод.')
            continue


def entering_data():  # Ввод данных при выборе 1. Добавить пользователя
    surname = input('Введите фамилию пользователя: ').capitalize()
    name = input('Введите имя пользователя: ').capitalize()
    phone_number = input('Введите номер телефона в формате (7XXXXXXXXXX): ')
    comment = input(
        'Введите комментарий или поставьте прочерк (-): ').capitalize()
    print('Информация успешно добавлена')
    return surname, name, phone_number, comment


def entering_dell_data():  # меню для  вызова удаления
    dell_data = int(input('Введите id абонента для удаления: '))
    return dell_data


def print_dell():
    print('Абонент успешно удален из базы данных')
    id = int(input('Введите id абонента для поиска: '))
    return id


def search_data_menu():  # меню для поиска
    while True:
        menu_search = input(
            'По какому критерию осущевлять поиск: \n1. id \n2. Номер телефона \n0. Завершить \n>')
        if menu_search == '1':
            search = int(input('Введите id абонента для поиска: '))
            return 1, search
        if menu_search == '2':
            search = input('Введите номер телефона в формате (7XXXXXXXXXX): ')
            return 2, search
        if menu_search == '0':
            sys.exit()
        else:
            print('Вы ввели неккоректное значение типа операции. Повторите ввод.')
            continue
