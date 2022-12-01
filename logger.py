from datetime import datetime as dt


def logger_write(sur, num, name, com):
    time = dt.now().strftime('%H:%H')
    with open('log.txt', 'a', encoding='utf8') as file:
        file.writelines(
            f'\nВремя внесения данных {time}, Фамилия = {sur}, Имя = {name}, Номер телефона = {num}, Комментарий = {com}')


def logger_search(a):
    time = dt.now().strftime('%H:%H')
    with open('log.txt', 'a', encoding='utf8') as file:
        file.writelines(
            f'\nВремя внесения данных {time}, информация по запрошенному поиску: {a}')


def logger_dell(id):
    time = dt.now().strftime('%H:%H')
    with open('log.txt', 'a', encoding='utf8') as file:
        file.writelines(
            f'\nВремя внесения данных {time}, удален пользователь: ', id)
