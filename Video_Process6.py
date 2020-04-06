import cv2
import numpy as np 

cap = cv2.VideoCapture('image/bida.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = 1000/fps

bg = cv2.createBackgroundSubtractorMOG2()

play = True
while True:
    if play:
        ret, img = cap.read()
    
    bg_mask = bg.apply(img)
    # bg_mask = cv2.merge((bg_mask, bg_mask, bg_mask))
    kernel = np.ones((5, 5))
    bg_mask = cv2.erode(bg_mask, kernel)
    bg_mask = cv2.dilate(bg_mask, kernel)
    bg_mask = cv2.medianBlur(bg_mask, 5, 0)

    #xu li vien
    img_c, contuor, hier = cv2.findContours(bg_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    s = []
    for c in contuor:
        s.append(cv2.contourArea(c))
    for i in range(len(s)):
        if s[i] > 800 and s[i] < 1000:
            cv2.drawContours(img, contuor[i], -1, (0, 0, 255), 2)

    # bg_mask = cv2.bitwise_and(img, bg_mask)


    cv2.imshow('Bida', img)
    cv2.imshow('Mask', bg_mask)
    key = cv2.waitKey(int(wait))
    if key == ord('q'):
        break
    if key == ord(' '):
        play = not play

cv2.destroyAllWindows()