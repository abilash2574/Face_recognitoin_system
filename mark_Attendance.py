import os
from datetime import datetime
from csv import reader


def mark_attendance(match_name):
    if not os.path.isfile('student_attendance.csv'):
        f = open('student_attendance.csv', 'w+')
        f.write('Name,Time')
        f.close()
    with open('student_attendance.csv', 'r+') as g:
        name_list = []
        csv_reader = reader(g)
        for line in csv_reader:
            name_list.append(line[0])
        if match_name not in name_list:
            current_time = datetime.now()
            date_format = current_time.strftime('%H:%M:%S')
            g.writelines(f'\n{match_name},{date_format}')


if __name__ == "__main__":
    mark_attendance('ABILASH_010')
