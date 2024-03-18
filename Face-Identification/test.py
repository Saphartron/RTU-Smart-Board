import cv2
import json
from face_identification import FaceIdentification as FC
#from face_identification import CreatePerson as Person

print("Testa Sākums!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------")
print("Git Checking!\n--------------------------------------------------------------2")

config = {}
with open("..\RTU-Smart-Board\Face-Identification\config.json","r") as jsonFile:
    config = json.loads(jsonFile.read())
#steves = Person("resources/dataset_photos/Steve","Steve Jobs")
tool = FC("/resources/Steve.jpg")
#tool.identify()
#write...