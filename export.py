import csv
import os.path



db_file_name = ''
db = []
global_id = 0  


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] != 'ID':
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        pass


def create(name='', surname='', number='', post=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("Неверный ввод!")
        return
    if(surname == ''):
        print("Неверный ввод!")
        return
    if(number == ''):
        print("Неверный ввод!")
        return
    if(post == ''):
        print("Неверный ввод!")
        return


    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, post.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)



def retrive(id='', name='', surname='', number='', post=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        # if(name != '' and row[1] != name.title()):
        #     continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(post != '' and row[4] != post.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Работник не найден'
    else:
        return result