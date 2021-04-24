import cv2
import face_recognition
import os


def create_image_list(path):
    dir_list = os.listdir(path)
    images_list = []
    for cl in dir_list:
        current_image = cv2.imread(f'{path}/{cl}')
        images_list.append(current_image)
    return images_list


def encode_images(images):
    encoded_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # the function expects a list so we use [0] for single image

        encode_image = face_recognition.face_encodings(img)[0]
        encoded_list.append(encode_image)
    return encoded_list
