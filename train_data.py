import cv2

def frame_formating(frame, face):
    for (x, y, h, w) in face:
        crop_img = frame[y+1:y+1 + h, x+1:x+1 + w]
        crop_img = cv2.resize(crop_img, (28, 28))        
    return crop_img

def get_trained_data(frame, face):
    obj = frame_formating(frame, face)
    data = []
    for i in range(obj.shape[0]):
        data.append([])
        for j in range(obj.shape[1]):
            data[i].append(obj[i][j])
    return data