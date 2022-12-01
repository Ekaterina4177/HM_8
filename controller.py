import sys
from view import get_menu_start, entering_data, entering_dell_data, print_dell, search_data_menu
from moduls import read_information_id, read_information_surname, write_info, read_information_id_dell, read_information_id_search, dell_information_id_search
from logger import logger_write, logger_search, logger_dell


def unification():
    menu_start = get_menu_start()
    if menu_start == 0:
        sys.exit()
    if menu_start == 1:
        sur, name, num, com = entering_data()
        max = read_information_id()
        #add_information(sur, name , num, com)
        write_info(max, sur, name, num, com)
        max = read_information_id_dell
        logger_write(sur, name, num, com)
    if menu_start == 2:
        try:
            id = entering_dell_data()
            read_information_id_dell(id)
            id = print_dell()
            dell_information_id_search(id)
        except FileNotFoundError:
            print('Не найдено')
        logger_dell(id)
    if menu_start == 3:
        value, search = search_data_menu()
        x = value
        y = search
        if x == 1:
            a = read_information_id_search(y)
        if x == 2:
            a = read_information_surname(y)
        logger_search(a)
