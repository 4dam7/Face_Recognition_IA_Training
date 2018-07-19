import tensorflow as ts
from tensorflow import keras
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/acohen/Projet_Perso/openCV/haarcascade_xml/haarcascade_frontalface_default.xml')

def frame_formating(frame, face):
    for (x, y, h, w) in face:
        crop_img = frame[y+1:y+1 + h, x+1:x+1 + w]
        crop_img = cv2.resize(crop_img, (28, 28))        
    return crop_img

def get_train_data(frame, face):
    obj = frame_formating(frame, face)
    cv2.imshow('data', obj)
    data = []
    for i in range(obj.shape[0]):
        data.append([])
        for j in range(obj.shape[1]):
            data[i].append(obj[i][j])
    return np.expand_dims(data, 0), 1