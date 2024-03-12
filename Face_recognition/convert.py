import os
import json
import dlib
import cv2

PREDICTOR_PATH = "1testFacecapt/bot/shape_predictor_68_face_landmarks.dat"

def detect_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = dlib.get_frontal_face_detector()

    faces = detector(gray)

    return faces

def extract_face_features(image, face):
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    landmarks = predictor(image, face)
    face_features = []

    for i in range(68):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        face_features.append((x, y))

    return face_features

def update_json_data(json_data, name, surname, face_features):
    data = {
        "group": group,
        "name": name,
        "surname": surname,
        "face_features": face_features
    }
    json_data.append(data)

if __name__ == "__main__":
    group = input("Noradi savu studiju programmu: ")
    name = input("Vards: ")
    surname = input("Uzvards: ")
    image_path = "1testFacecapt/f3.jpg"
    output_dir = "1testFacecapt"
    output_file = os.path.join(output_dir, "data.json")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = cv2.imread(image_path)
    faces = detect_face(image_path)

    if len(faces) == 0:
        print("Лицо не обнаружено на изображении.")
    else:
        if os.path.exists(output_file):
            with open(output_file, "r") as file:
                json_data = json.load(file)
        else:
            json_data = []

        for face in faces:
            face_features = extract_face_features(image, face)
            update_json_data(json_data, name, surname, face_features)

        with open(output_file, "w") as file:
            json.dump(json_data, file, indent=4)

        print("Paldies", name, surname, "tu esi registrets!")
