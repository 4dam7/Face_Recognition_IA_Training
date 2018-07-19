import sys
from train_data import get_trained_data
from save_data import save_data

# detection of face + use of webcam
import cv2

# keyboard imput
import keyboard

# error if the is no name
if len(sys.argv) != 2 :
    print("usage :\n python3", sys.argv[0], "\"name\"")

# preparing webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
# exit variable
want_to_quit = 0
# list of images
new_data = []

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
    cv2.waitKey(1)
    
    # add an image into the list
    if keyboard.is_pressed(' ') and len(face) == 1 :
        new_data.append(get_trained_data(gray, face))
        
    # quit
    if keyboard.is_pressed('q') :
        want_to_quit = 1

save_data(new_data, sys.argv[1])
print(sys.argv[1], "has been saved in the database !")