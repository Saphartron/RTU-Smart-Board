import dlib
import cv2
import json
import os
from skimage import io

sp = dlib.shape_predictor('bot/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('bot/dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
face_cascade = cv2.CascadeClassifier('bot/haarcascade_frontalface_default.xml')

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
    print("Ievadiet kursu: ")
    print("Pemēram Informacijas Tehnologijas")
    group = input("")
    print("Ievadi apmācibas gadu: ")
    ynumber = input("")
    print("Ievadiet grupas numuru: ")
    number = input("")
    print("Ievadiet vārdu: ")
    name = input("")
    print("Ievadiet uzvārdu: ")
    surname = input("")
    
    img1 = io.imread('f2.jpg')
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
