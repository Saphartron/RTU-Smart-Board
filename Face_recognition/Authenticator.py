import dlib
import cv2
import json
import os
import time
from scipy.spatial import distance

sp = dlib.shape_predictor('bot/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('bot/dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
face_cascade = cv2.CascadeClassifier('bot/haarcascade_frontalface_default.xml')

def register():
    def update_json_data(json_data, group, number, name, surname, face_descriptor):
        face_descriptor_list = [value for value in face_descriptor]
        
        data = {
            "group": group,
            "number": number,
            "name": name,
            "surname": surname,
            "face_features": face_descriptor_list
        }
        json_data.append(data)
        
    if __name__ == "__main__":
        group = input("Ievadiet savu kursu: ")
        number = input("Ievadiet grupas numuru: ")
        name = input("Ievadiet Jūsu vārdu: ")
        surname = input("Ievadiet Jūsu uzvārdu: ")
        


        def det_f(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
                        
            if len(faces) > 0:
                return True
            else:
                return False
                            
        cam = cv2.VideoCapture(0)
        print ("Tiek veikta registrācija")
        screen = None
        while True:
            ret, frame = cam.read()
            if ret:
                if det_f(frame):
                    screen = frame.copy()
                    break
                else:
                    print("Jūsu seja nav atpazīta, lūdzu skataties uz kameru!")
                    time.sleep(1.5)
                    
        dets = detector(screen, 1)
        for k, d in enumerate(dets):
            shape = sp(screen, d)
            face_descriptor = facerec.compute_face_descriptor(screen, shape)
                            
        cam.release()
        cv2.destroyAllWindows()
                
                   

        output_dir = ""
        output_file = os.path.join(output_dir, "data.json")

        if os.path.exists(output_file):
            with open(output_file, 'r') as json_file:
                json_data = json.load(json_file)
        else:
            json_data = []

        update_json_data(json_data, group, number, name, surname, face_descriptor)

        with open(output_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print("Paldies", name, surname, "tu esi registrets!")
                
        


def authentication():
    with open('data.json', 'r') as file:
        data = json.load(file)
    matchees = []

    def detect_faces(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(150, 150))
        
        if len(faces) > 0:
            return True
        else:
            return False
        
    cap = cv2.VideoCapture(0)
    print("Tiek veikta autentifikācija")
    screenshot = None

    while True:
        ret, frame = cap.read()
        if ret:
            if detect_faces(frame):
                screenshot = frame.copy()
                break
            else:
                print("Jūsu seja nav atpazīta, lūdzu skataties uz kameras pusi!")
                time.sleep(1.5)
                
    dets_webcam = detector(screenshot, 1)
            
    for k, d in enumerate(dets_webcam):
        shape = sp(screenshot, d)
        face_descriptor2 = facerec.compute_face_descriptor(screenshot, shape)

    for person in data:
        a = distance.euclidean(person['face_features'], face_descriptor2)
        if a < 0.551:
            matchees.append({
                'group': person["group"],
                'number': person["number"],
                'name': person['name'],
                'surname': person['surname']
                
            })
    
    while True:        
        match matchees:
            case []:
                print("Nav atrastas līdzības, meiginiet vēl reiz!")
                authentication()
            case _:
                for match in matchees:
                    print("Grupa: ", match['group'], match['number'])
                    print("Vārds Uzvārds ", match['name'],match['surname'])
                cap.release()
                cv2.destroyAllWindows()
                print (a)
                break 
        break
    
while True:
    chose = input("Ja esi registēts izvēlies (2), ja neesi registrēts tad izvēlies (1):  ")
    match chose:
        case '1':
            register()
        case '2':
            authentication()
        case "off":
            break
        case _:
            print("Ievadita nepareiza izvēle!")
