import cv2
import numpy as np 


def Min_Blue(pos):
    Min_Blue.value = pos
Min_Blue.value = 0

def Min_Green(pos):
    Min_Green.value = pos
Min_Green.value = 82

def Min_Red(pos):
    Min_Red.value = pos
Min_Red.value = 7


def Max_Blue(pos):
    Max_Blue.value = pos
Max_Blue.value = 117

def Max_Green(pos):
    Max_Green.value = pos
Max_Green.value = 201

def Max_Red(pos):
    Max_Red.value = pos
Max_Red.value = 100


cv2.namedWindow('Control')
cv2.createTrackbar('Min Blue', 'Control', 0, 255, Min_Blue)
cv2.createTrackbar('Min Green', 'Control', 0, 255, Min_Green)
cv2.createTrackbar('Min Red', 'Control', 0, 255, Min_Red)

cv2.createTrackbar('Max Blue', 'Control', 255, 255, Max_Blue)
cv2.createTrackbar('Max Green', 'Control', 255, 255, Max_Green)
cv2.createTrackbar('Max Red', 'Control', 255, 255, Max_Red)

cap = cv2.VideoCapture('image/tracking.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
wait = 1000/fps

play = True
while True:
    if play:
        ret, img = cap.read()
        cv2.imshow('Control', img)
    if ret == False:
        break

    lower = np.array([Min_Blue.value, Min_Green.value, Min_Red.value])
    upper = np.array([Max_Blue.value, Max_Green.value, Max_Red.value])
    mask_sub = cv2.inRange(img, lower, upper) # trong khoang lower->upper thi mask = 1, or no mask = 0
    
    #Khu nhieu bang xoi mon erode:
    # kernel = np.ones((4, 4))
    # mask_sub = cv2.erode(mask_sub, kernel)
    mask_sub = cv2.medianBlur(mask_sub, 5)

    #Dilate phong to
    kernel2 = np.ones((7, 7))
    mask_sub = cv2.dilate(mask_sub, kernel2)

    mask = cv2.merge((mask_sub, mask_sub, mask_sub)) 
    res = cv2.bitwise_and(img, mask) #1 and 1 = 1 (1 ^ 1 =1)
    
    cv2.imshow('Mask', mask_sub)
    cv2.imshow('Result', res)

    key = cv2.waitKey(int(wait))
    if key == ord('q'):
        break
    if key == ord(' '):
        play = not play
        
cv2.destroyAllWindows