import dlib
import cv2
import json
import os
from skimage import io

sp = dlib.shape_predictor('Authenticator/bot/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('Authenticator/bot/dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
face_cascade = cv2.CascadeClassifier('Authenticator/bot/haarcascade_frontalface_default.xml')

def update_json_data(json_data, group, number, name, surname, face_descriptor):
    face_descriptor_list = [value for value in face_descriptor]
    
    data = {
        "group": group,
        "number":number,
        "name": name,
        "surname": surname,
        "face_features": face_descriptor_list
    }
    json_data.append(data)

if __name__ == "__main__":
    group = input("Ievadiet kursu: ")
    number = input("Ievadiet numuru: ")
    name = input("Ievadiet vārdu: ")
    surname = input("Ievadiet uzvārdu: ")
    img1 = io.imread('testfavecapt/f8.jpg')
    dets = detector(img1, 1)

    for k, d in enumerate(dets):
        shape = sp(img1, d)
        face_descriptor = facerec.compute_face_descriptor(img1, shape)

    output_dir = ""
    output_file = os.path.join(output_dir, "data.json")

    if os.path.exists(output_file):
        with open(output_file, 'r') as json_file:
            json_data = json.load(json_file)
    else:
        json_data = []

    update_json_data(json_data, group, number, name, surname, face_descriptor)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print(name, surname, "ir registrets!")
