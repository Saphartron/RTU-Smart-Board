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
class CreatePerson:
    #constructor
    def __init__(self,datasetUrl,Name) -> None:
        self.folder = datasetUrl
        self.Name = Name
        pass
    
    
    def createPerson(self,getPhotoDir,saveDir):
        for images in os.listdir(getPhotoDir):
                for img_path in image_files_in_folder(os.path.join(getPhotoDir,images)):
                     image = face_recognition.load_image_file(img_path)
                     break
        #write...
        pass
    def train():
         #write...
         pass