import os
from datetime import datetime
from csv import reader


def mark_attendance(match_name):
    filename=f'Attendance/{datetime.now().strftime("%d-%B-%Y")}_attendance.csv'
    if not os.path.isfile(filename):
        f = open(filename, 'w+')
        f.write('Name,Time')
        f.close()
    with open(filename, 'r+') as g:
        name_list = []
        csv_reader = reader(g)
        for line in csv_reader:
            name_list.append(line[0])
        if match_name not in name_list:
            current_time = datetime.now()
            date_format = current_time.strftime('%H:%M:%S')
            g.writelines(f'\n{match_name},{date_format}')


if __name__ == "__main__":
    # print(datetime.now())
    mark_attendance('ABILASH_010')
    mark_attendance('GARYVEE_003')
    mark_attendance('VISHENLAKHIANI_009')
