import cv2

def frame_formating(frame, face):
    objs = []
    for (x, y, h, w) in face:
        crop_img = frame[y+1:y+1 + h, x+1:x+1 + w]
        crop_img = cv2.resize(crop_img, (28, 28))
        objs.append(crop_img)
    return objs

def get_train_data(frame, face):
    objs = frame_formating(frame, face)
    data = []
    a = -1
    for n in range(len(objs)):
        objs.append([])
        a += 1
        for i in range(objs[n].shape[0]):
            data.append([])
            for j in range(objs[n].shape[1]):
                data[a][i].append(objs[n][i][j])
    return data