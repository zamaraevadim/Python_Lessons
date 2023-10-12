from logger import *
def user_interface():
    with open('phonebook.txt','a', encoding='utf-8'):
        pass
    cmd = None
    while cmd != '4':
        print('Меню: \n'
            '1. Запись данных\n'
            '2. Вывести данные на экран\n'
            '3. Поиск контакта\n'
            '4. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1','2','3','4'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contact()
            case '3':
                search_contact()