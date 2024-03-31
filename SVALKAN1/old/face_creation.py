import os
import cv2
import dlib
from face_identification import DataBase


class FaceCreation:
    def __init__(self,filePath,database: DataBase) -> None:
        self.faceDetector = dlib.get_frontal_face_detector()
        self.facerec = dlib.face_recognition_model_v1('Face-Identification\\dlib_face_recognition_resnet_model_v1.dat')
        self.sp = dlib.shape_predictor('Face-Identification\\shape_predictor_68_face_landmarks.dat')
        self.filePath = filePath
        self.database = database
        pass
    def dataConverter(self):
        photo = cv2.imread(filename=self.filePath)
        dets = self.faceDetector(photo,1)
        face_descriptor = None
        
        for k, d in enumerate(dets):
            shape = self.sp(photo, d)
            face_descriptor = self.facerec.compute_face_descriptor(photo, shape)
            
        face_descriptor_list = [value for value in face_descriptor]
        return face_descriptor_list
    
    def getAbout(self,data:dict):
        self.database.add(data)
        pass
    
    def dataBaseLength(self):
        return self.database.dataBaseLenght()
    
    def save(self):
        self.database.saveData()
        pass

database = DataBase(os.getcwd() + "\\Face-Identification\\resources\\savedModels.json")
create = FaceCreation(os.getcwd()+"\\Face-Identification\\resources\\dataset_photos\\Steve.jpg", database)
create.getAbout(
    {
        "Id": create.dataBaseLength(),
        "Name": input("Name: "),
        "Surname": input("Surname: "),
        "Grupa": input("Grupa: "),
        "Data": create.dataConverter()
    }
    )
create.save()
print("Finish!")