import face_recognition
import os
import cv2
from face_recognition.face_recognition_cli import image_files_in_folder

class FaceIdentification:
    #constructor
    def __init__(self,photoUrl: str,config) -> None:
        self.photo = face_recognition.load_image_file(photoUrl)
        self.configuration = config
        pass
    
    
    def identify(self):
        #write...
        pass
    def tmpresult(self):
        #
        pass
class CreatePerson:
    #constructor
    def __init__(self,config:dict,Name:str) -> None:
        self.configuration = config
        self.Name = Name
        pass
    
    def createPerson(self):
        filesUrl = self.configuration.get("dataSetUrl")
        something = []
        for images in os.listdir(filesUrl):
                for img_path in image_files_in_folder(os.path.join(filesUrl,images)):
                     something.append(img_path)
        #write...
        pass
    def train():
         #write...
         pass