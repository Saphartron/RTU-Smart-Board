import cv2
import time
import os
from face_identification import FaceIdentification as FC
#from face_identification import DataBase as DS
import sys
print(sys.path)

cap = cv2.VideoCapture(0)

#database = DS(os.getcwd() + "\\Face-Identification\\resources\\savedModels.json")
#tool = FC(database=database)
#while True:
#    tool.setPhoto(cap.read())
#tool.identify()
#write...