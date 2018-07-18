import tensorflow as ts
from tensorflow import keras
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/acohen/Projet_Perso/openCV/haarcascade_xml/haarcascade_frontalface_default.xml')
network = keras.Sequential(
])


def frame_formating(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    a = 0
    for (x, y, h, w) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crop_img = gray[y+1:y+1 + h, x+1:x+1 + w]
        crop_img = cv2.resize(crop_img, (28, 28))
        break        
        a = 1
    if a == 0:
        return gray, 0
    return crop_img, 1

def convert_to_data_arr(frame):
    obj, err = frame_formating(frame)
    if err == 0:
        return obj, 0
    cv2.imshow('data', obj)
    data = []
    for i in range(obj.shape[0]):
        data.append([])
        for j in range(obj.shape[1]):
            data[i].append(obj[i][j]) 
    return np.expand_dims(data, 0), 1

while (True):
    ret, frame = cap.read()
    data, err = convert_to_data_arr(frame)            
    if err == 0:
        continue 
    cv2.imshow('feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




    