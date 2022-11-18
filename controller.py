from import_dt import import_dt
from export_dt import export_dt
from search_dt import search_dt
from output_dt import output_dt

def greeting():
    print('Hello! Welcome to "PhoneBook" app!')

def input_dt():
    surname = input('Enter surname: ')
    first_name = input('Enter name: ')
    middle_name = input('Enter middle-name: ')
    birth_date = input('Enter your birth date (dd.mm.yyyy): ')
    phone_number = input('Enter phone number: ')
    description = input('Enter description: ')
    return [surname, first_name, middle_name, birth_date, phone_number, description]

def sep_choice():
    sep = input('Enter separation symbol: ')
    if sep == '':
        sep = None
    return sep

def main_menu():
    print('Available options:\n1 - Add contact\n2 - Show all contacts\n3 - Find contact')
    option = input('Choose option: ')
    if option == '1':
        sep = sep_choice()
        import_dt(input_dt(), sep)
    elif option == '2':
        data = export_dt()
        output_dt(data)
    else:
        word = input('Enter data to find: ')
        data = export_dt()
        item = search_dt(word, data)
        if item != None:
            print('Surname'.center(10), 'Name'.center(10), 'Middle-Name'.center(20), 'Date of Birth'.center(20), 'Phone Number'.center(20), 'Description'.center(20))
            print('*' * 110)
            print(item[0].center(10), item[1].center(10), item[2].center(20), item[3].center(20), item[4].center(20), item[5].center(20))
        else:
            print('No matches found. Please try again')
