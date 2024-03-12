import cv2
from face_identification import FaceIdentification as FC
from face_identification import CreatePerson as Person

print("Testa Sākums!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------2")

steves = Person("resources/dataset_photos/Steve","Steve Jobs")
tool = FC("/resources/Steve.jpg")
tool.identify()
#write...