import export as cr



print('\nДобро пожаловать в БД')


def ls_menu():
    while True:
        print('\nВыберите пункт меню:\n'
              '1. Отобразить весь справочник.\n'
              '2. Найти сотрудника по вамилии.\n'
              '3. Найти сотрудника по должности.\n'
              '4. Найти сотрудника по номеру.\n'
              '5. Добавить нового сотрудника.\n'
              '6. Закрыть программу.')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            print(cr.retrive())

        elif n == 2:
            search = input('Введите фамилию: ')
            print(cr.retrive(surname=search))

        elif n == 3:
            search = input('Введите должность: ')
            print(cr.retrive(post=search))

        elif n == 4:
            search = input('Введите номер  телефона: ')
            print(cr.retrive(number=search))

        elif n == 5:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            post = input('Введите должность. ')
            cr.create(name, surname, number, post)

        elif n == 6:
            print('Спасибо за работу!')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)