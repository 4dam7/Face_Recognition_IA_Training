# TenserFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# detection of face + use of webcam
import cv2

# Helper Librairies
import numpy as np


train_images, train_labels, names = get_data()

# create a neural network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(len(names), activation=tf.nn.softmax)
])

# giving the network rules
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# training
model.fit(train_images, train_labels, epochs=5)

# preparing webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
# exit variable
want_to_quit = 0

while not want_to_quit :
    ret, frame = cap.read()

    # getting face position
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 7)

    # printing all squares around faces
    for (x, y, w, h) in face :
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
    
    # print cam
    cv2.imshow("cam", frame)
    cv2.waitKey(10)

    if len(face) > 0 :
        # recup les personnes qui sont presentes
        persons_seen = []
        for person in persons_seen :
            if (person != "unknown")
        print("let's see who's here")

    # quit
    if keyboard.is_pressed('q') :
        want_to_quit = 1
