from logger import *
def user_interface():
    with open('phonebook.txt','a', encoding='utf-8'):
        pass
    cmd = None
    while cmd != '6':
        print('Меню: \n'
            '1. Запись данных\n'
            '2. Вывести данные на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить данные\n'
            '5. Удалить данные\n'
            '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1','2','3','4','5','6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contact()
            case '3':
                print(search_contact())
                print()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            