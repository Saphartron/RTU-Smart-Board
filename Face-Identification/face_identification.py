import face_recognition
import os
from face_recognition.face_recognition_cli import image_files_in_folder

class FaceIdentification:
    def __init__(self,photoUrl: str) -> None:
        self.photo = face_recognition.load_image_file(photoUrl)
        print(self.photo)
        pass
    def createPerson(self,getPhotoDir,saveDir):
        for images in os.listdir(getPhotoDir):
                for img_path in image_files_in_folder(os.path.join(getPhotoDir,images)):
                     image = face_recognition.load_image_file(img_path)
                     break
        pass