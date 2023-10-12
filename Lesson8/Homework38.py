# Создать телефонный справочник
# 1. UI
# 2. Создать файл
# 3. Читать файл
# 4. Вывод данных на экран:
#     - считать файл
#     - сохранить в переменной
#     - вывод на экран
# 5. Запись контакта:
#     - запросить данные
#     - сохранить в переменной
#     - записать в файл
# 6. Поиск контакта:
#     - запросить данные
#     - сохранить в переменной
#     - считать файл
#     - сохранить в переменной
#     - произвести поиск


# def name_data():
#     return input('Введите имя: ')

# def surname_data():
#     return input('Введите фамилию: ')

# def patronymic_data():
#     return input('Введите отчество: ')

# def phone_number_data():
#     return input('Введите номер: ')

# def address_data():
#     return input('Введите адрес: ')

# def input_contact():
#     name = name_data()
#     surname = surname_data()
#     patronymic = patronymic_data()
#     phone_number = phone_number_data()
#     address = address_data()

#     return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'

# def add_contact():
#     contact = input_contact()
#     with open('phonebook.txt','a', encoding='utf-8') as data:
#         data.write(contact + '\n\n')

# def read_file():
#     with open('phonebook.txt','r', encoding='utf-8') as data:
#         return data.read()

# def print_contact():
#     data = read_file()
#     print([data])

# def search_contact():
    
#     print()
#     print('Варианты поиска: \n'
#             '1. По имени\n'
#             '2. По фамилии \n'
#             '3. По отчеству\n'
#             '4. По телефону\n'
#             '5. По адресу')
#     choice = input('Выберите вариант поиска: ')
#     choice = int(choice) - 1
#     search = input('Введите данные для поиска: ')
#     contacts_str = read_file().rstrip()
#     if search not in contacts_str:
#         print('Не найдено')
#     else:
        
#         contacts_lst = contacts_str.split('\n\n')
        
#         for el_str in contacts_lst:
#             el_lst = el_str.replace('\n',' ').split()
#             if search in el_lst[choice]:
#                 print(el_lst)
#                 print()

# def user_interface():
#     with open('phonebook.txt','a', encoding='utf-8'):
#         pass
#     cmd = None
#     while cmd != '4':
#         print('Меню: \n'
#             '1. Запись данных\n'
#             '2. Вывести данные на экран\n'
#             '3. Поиск контакта\n'
#             '4. Выход')
#         cmd = input('Введите номер операции: ')
#         while cmd not in ('1','2','3','4'):
#             print('Некорректный ввод')
#             cmd = input('Введите номер операции: ')
#         match cmd:
#             case '1':
#                 add_contact()
#             case '2':
#                 print_contact()
#             case '3':
#                 search_contact()

# user_interface()
