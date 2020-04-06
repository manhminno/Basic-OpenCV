import cv2 
import numpy as np 

cap = cv2.VideoCapture('image/tracking.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = 1000/fps
arr_point = np.array((), np.int32)

play = True
while True:
    if play:
        ret, img = cap.read()
    if img is None:
        img = tmp_img
    else:
        tmp_img = img
    
    #tao mask
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([33, 50, 62])
    upper = np.array([102, 255, 245])
    mask = cv2.inRange(img_hsv, lower, upper)
    #Khu nhieu mask
    kernel_erode = np.ones((3, 3))
    mask = cv2.erode(mask, kernel_erode)
    mask = cv2.dilate(mask, kernel_erode)
    mask = cv2.medianBlur(mask, 5, 0)

    #Ve vien va quy dao
    img_copy = img.copy()
    img_c, contuors, hier = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if len(contuors) > 0:
        tmp_c = contuors[0]
        (cx, cy), r = cv2.minEnclosingCircle(tmp_c)
        res = cv2.circle(img_copy, (int (cx), int(cy)), int(r/1.25), (0, 0, 255), 2)
        arr_point = np.append(arr_point, (int(cx), int(cy)))
        if len(arr_point) > 1000:
            arr_point = np.delete(arr_point, (0, 1))
        arr_point = arr_point.reshape((-1 ,1, 2))
        cv2.polylines(img_copy, [arr_point], False, (255, 0, 0), 2)


    cv2.imshow('Result', img_copy)
    cv2.imshow('Video', img)
    key = cv2.waitKey(int(wait))
    if key == ord('q'):
        break
    elif key == ord(' '):
        play = not play

cv2.destroyAllWindows()