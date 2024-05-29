from date_create import *


def input_data():
    name = name_data2()
    surname = surname_data2()
    phone = phone_data2()
    address = address_data2()
    var = int(input(f'в каком формате записать данные\n' 
                    f'1 вариант\n'
                    f'{name}\n{surname}\n{phone}\n{address}\n'
                    f'2 вариант\n'
                    f'{name};{surname};{phone};{address}\n'))
    while var != 1 and var != 2:
        print('не верная команда')
        var = int(input("Введите команду"))
    
    if var == 1:
        with open('data_first_variant.csv', 'a',encoding='utf=8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    if var == 2:
        with open('data_second_variant.csv', 'a',encoding='utf=8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r',encoding='utf=8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r',encoding='utf=8') as f:
        data_second = f.readlines()
        print(*data_second)


def edit_data():
    print(f'в какой фаил вы хотите изменить?\n'
          f'1 - data_first_variant.csv\n'
          f'2 - data_second_variant.csv')
    edit = int(input('введите номер файла\n'))
    while edit != 1 and edit != 2:
        print('не верная команда')
        edit = int(input("Введите команду"))

    if edit == 1:
        with open('data_first_variant.csv', 'r',encoding='utf=8') as f:
            data_first = f.readlines()
            print("вывожу запись на экран\n")
            print(''.join(data_first))
            print('Введите данные для замены\n')
            old_name = old_name_data()            
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            index = data_first.index(old_name)
            data_first[index] = name
            data_first[index+1] = surname
            data_first[index+2] = phone
            data_first[index+3] = address
        with open('data_first_variant.csv', 'a',encoding='utf=8') as f:
            for i in data_first:
                f.write(i)
    
    elif edit == 2:
        with open('data_second_variant.csv', 'r',encoding='utf=8') as f:
            data_first = f.readlines()
            print("вывожу запись на экран\n")
            print(data_first)
            index = int(input('выберите запись для редактирования ')) - 1
            if data_first[index] == '\n':
                index += 1

            name = name_data2()
            surname = surname_data2()
            phone = phone_data2()
            address = address_data2()

            data_first[index] = f'{name};{surname};{phone};{address}\n'
        with open('data_second_variant.csv', 'a',encoding='utf=8') as f:
            for i in data_first:
                f.write(i)
                      
            
def del_data():
    print(f'в какой фаил вы хотите изменить?\n'
          f'1 - data_first_variant.csv\n'
          f'2 - data_second_variant.csv')
    comands = int(input('введите номер файла\n'))
    while comands != 1 and comands != 2:
        print('не верная команда')
        comands = int(input("Введите команду"))
    
    if comands == 1:
        with open('data_first_variant.csv', 'r',encoding='utf=8') as f:
            data_first = f.readlines()
            print("вывожу запись на экран\n")
            print(''.join(data_first))
            print('Введите ИМЯ для УДАЛЕНИЯ\n')
            old_name = old_name_data()  
            index = data_first.index(old_name)
            for i, item in enumerate(data_first[index:index+5]):
                data_first.remove(item)
            print(''.join(data_first))
        with open('data_first_variant.csv', 'w',encoding='utf=8') as f:
            for i in data_first:
                f.write(i)
    
    elif comands == 2:
        with open('data_second_variant.csv', 'r',encoding='utf=8') as f:
            data_first = f.readlines()
            print("вывожу запись на экран\n")
            print(''.join(data_first))
            index = int(input('выберите запись для УДАЛЕНИЯ ')) - 1
            if data_first[index] == '\n':
                index += 1
                data_first.pop(index)
            else:    data_first.pop(index)
        with open('data_second_variant.csv', 'w',encoding='utf=8') as f:
            for i in data_first:
                f.write(i)




del_data()