from logger import *

def interface():
    print('Добрый день! Вы попали на специальный бот справочник \n 1 - запись данный \n 2 - вывод данных \n 3 - изменить данные \n 4 - удалить данные')
    comand = int(input("Введите команду\n"))

    while comand != 1 and comand != 2 and comand != 3 and comand != 4:
        print('не верная команда')
        comand = int(input("Введите команду\n"))

    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3:
        edit_data()
    elif comand == 4:
        del_data()

interface()