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
        face_encoding = face_recognition.face_encodings(self.photo)[0]

        small_frame = cv2.resize(None, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
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