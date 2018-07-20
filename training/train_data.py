import cv2
import keyboard

mode = -1

def frame_formating(frame, face):
    objs = []  
    global mode
    #frame_formating.mode += 1  
    for (x, y, h, w) in face:
        crop_img = frame[y+1:y+1 + h, x+1:x+1 + w]
        crop_img = cv2.resize(crop_img, (28, 28))
        objs.append(crop_img)
    if (keyboard.is_pressed(' ')):
        mode = mode * -1
    if mode > 0:
        for i in range(len(objs)) :
            cv2.imshow("Face " + str(i + 1), objs[i])
    else :
        for i in range(len(objs)) :
            cv2.destroyWindow("Face " + str(i + 1))
    return objs

def get_train_data(frame, face):
    objs = frame_formating(frame, face)
    data = []    
    for elements in objs :
        data.append(elements)
    return data