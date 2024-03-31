import dlib
import json
import threading
import numpy
from scipy.spatial import distance

class FaceIdentification:
    #constructor
    def __init__(self,database: 'DataBase') -> None:
        self.faceDetector = dlib.get_frontal_face_detector()
        self.facerec = dlib.face_recognition_model_v1('Face-Identification\\dlib_face_recognition_resnet_model_v1.dat')
        self.sp = dlib.shape_predictor('Face-Identification\\shape_predictor_68_face_landmarks.dat')
        self.database = database
        self.var = []
        pass
    def setPhoto(self,photo):
        self.face_descriptor = None
        dets_webcam = self.faceDetector(photo, 1)
            
        for k, d in enumerate(dets_webcam):
            shape = self.sp(photo, d)
            self.face_descriptor = self.facerec.compute_face_descriptor(photo, shape)
        pass
    
    def identify(self)-> dict:
        self.var = []
        if self.face_descriptor == None:
            t1 = threading.Thread(target=self.loop,args=(self.database.dataLS,0,self.database.dataLS.__len__()/2))
            t2 = threading.Thread(target=self.loop,args=(self.database.dataLS,self.database.dataLS.__len__()/2,self.database.dataLS.__len__()))
            t1.start()
            t2.start()
            if self.var.count == 0:
                return None
            return self.min()
        return None
    def min(self):
        m = [0,1]
        for i in self.var:
            if i[1]<m[1]:
                m = i
        return m 
    def loop(self,list:list,fromI,range):
        for v in list[fromI:range]:
            more = distance.euclidean(self.database.getData(v).person['Data'], self.face_descriptor)
            if more< 0.5:
                self.var.append([v.Id,more])
            
        
class DataBase:
    def __init__(self,filePath:str) -> None:
        self.filePath = filePath
        self.dataLS = []
        with open(self.filePath,"r") as jsonFile:
            self.dataLS = json.loads(jsonFile.read())
        pass
    def add(self,new):
        self.dataLS.append(new)
        pass
    def dataBaseLenght(self):
        return self.dataLS.__len__()
    def getData(self,id):
        return  self.dataLS[id]
    def saveData(self):
        with open(self.filePath,"w") as jsonFile:
            ls = json.dumps(self.dataLS)
            jsonFile.write(ls)
        pass
        return 
    