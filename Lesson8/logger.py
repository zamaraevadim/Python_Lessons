from data_create import *
def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()

    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'

def add_contact():
    contact = input_contact()
    with open('phonebook.txt','a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_file():
    with open('phonebook.txt','r', encoding='utf-8') as data:
        return data.read()

def print_contact():
    data = read_file()
    print(data)

def search_contact():
    
    print()
    print('Варианты поиска: \n'
            '1. По имени\n'
            '2. По фамилии \n'
            '3. По отчеству\n'
            '4. По телефону\n'
            '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    contacts_str = read_file().rstrip()
    if search not in contacts_str:
        print('Не найдено')
    else:
        
        contacts_lst = contacts_str.split('\n\n')
        
        for el_str in contacts_lst:
            el_lst = el_str.replace('\n',' ').split()
            if search in el_lst[choice]:
                return el_lst
                

def change_contact():
            print("Выберите контакт для изменения: ")
            contact = search_contact()
            contacts_str = read_file().rstrip()
            contacts_str = contacts_str.split('\n\n')
            count = 0
            for el in contacts_str:
                elem = el.replace('n',' ').split()
                if contact == elem:
                    break
                count += 1
            print(contact)
            print()
            print('Выберете что хотите изменить: ')
            cmd = None
            while cmd != '6':
                 print('Меню: \n'
                '1. Имя\n'
                '2. Фамилию\n'
                '3. Отчество\n'
                '4. Номер\n'
                '5. Адрес\n'
                '6. Выход в меню\n')
                 cmd = input('Введите номер операции: ')
            
                 while cmd not in ('1','2','3','4','5','6'):
                    print('Некорректный ввод')
                    cmd = input('Введите номер операции: ')
                 match cmd:
                    case '1':
                        
                        new_name = input('Введите новое имя: ')
                        contact[int(0)] = new_name
                        contacts_str[count] = contact
                        
                    case '2':
                        new_name = input('Введите новую фамилию: ')
                        contact[int(1)] = new_name
                        contacts_str[count] = contact
                        
                    case '3':
                        new_name = input('Введите новое отчество: ')
                        contact[int(2)] = new_name
                        contacts_str[count] = contact
                        
                            
                    case '4':
                        new_name = input('Введите новый номер: ')
                        contact[int(3)] = new_name
                        contacts_str[count] = contact
                        
                    case '5':
                        new_name = input('Введите новый адрес: ')
                        contact[int(4)] = new_name
                        contacts_str[count] = contact
                 file = open('phonebook.txt','a')
                 file.seek(0)
                 file.truncate()
                 file.close()
                 for contact1 in contacts_str:
                     if not isinstance(contact1,list):
                         contact1 = contact1.split()        
                     with open('phonebook.txt','a', encoding='utf-8') as data:
                             data.write(f'{contact1[0]} {contact1[1]} {contact1[2]}\n{contact1[3]}\n{contact1[4]}' + '\n\n')
                        
                
            
def delete_contact():
    print()