def import_dt(data, sep=None):
    with open('phonebook.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f'{i}\n')
            file.write(f'\n')
        else:
            file.write(sep.join(data))
            file.write(f'\n')
