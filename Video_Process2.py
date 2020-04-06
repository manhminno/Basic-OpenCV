import cv2
import numpy as np 

cap = cv2.VideoCapture('image/tracking.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = 1000/fps

play = True
while True:
    if play:
        ret, img = cap.read()
    if img is None:
        img = tmp_img
    else:
        tmp_img = img
    cv2.imshow('Video', img)

    #tao Mask
    img_clone = img.copy()
    img_hsv = cv2.cvtColor(img_clone, cv2.COLOR_BGR2HSV)
    lower = np.array([33, 50, 62])
    upper = np.array([102, 255, 248])
    mask = cv2.inRange(img_hsv, lower, upper)

    #Khu nhieu mask, va dilate
    mask = cv2.medianBlur(mask, 5)
    kernel_dilate = np.ones((5, 5))
    mask = cv2.dilate(mask, kernel_dilate)

    #Find vat the
    img_contours, contours, hier = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    #Ve vien
    if len(contours) > 0:
        tmp_c = contours[0] #lay cac duong vien cua vat the 1
        M = cv2.moments(tmp_c) #trich xuat dac trung
        img_clone = cv2.drawContours(img_clone, contours, -1, (0, 0, 255), 2)
        
        #tim tam de puttext
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        cv2.putText(img_clone, 'Ball', (x+7, y-7), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    
    cv2.imshow('Result', img_clone)

    key = cv2.waitKey(int(wait))
    if key == ord('q'):
        break
    if key == ord(' '):
        play = not play
cv2.destroyAllWindows()