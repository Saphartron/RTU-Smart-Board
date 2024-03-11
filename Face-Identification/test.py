import cv2
from face_identification import FaceIdentification as FC

print("Testa Sākums!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------2")

tool = FC("/resources/Steve.jpg")
tool.createPerson("/resources/dataset_photos","/resources/models")