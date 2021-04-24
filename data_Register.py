import face_recognition_functions as fr
import os
import pandas as pd


def get_students_details(dir_path):
    students_details = []
    dir_list = os.listdir(dir_path)
    for cl in dir_list:
        students_details.append(os.path.splitext(cl)[0])
    return students_details


def export_as_csv(encoded_image_list, students_detail_list):
    student_data = pd.DataFrame(encoded_image_list, index=students_detail_list)
    student_data.to_csv(r'Student_data.csv')
    print('Exported File')
    return None


def encode_image(d_path):
    encoded_image_list = fr.encode_images(fr.create_image_list(d_path))
    print('Encoded image')
    return encoded_image_list


def start_data_registry(di_path):
    dir_path = di_path
    export_as_csv(encode_image(dir_path), get_students_details(dir_path))
    print('Data has been updated')


