import cv2
import numpy as np 

def get_value(pos):
    get_value.value = pos

get_value.value = 0

cv2.namedWindow("Control")
cv2.createTrackbar("Value: ", "Control", 0, 255, get_value)

while True:
    img = cv2.imread('image/image1(1).jpeg')
    img = cv2.resize(img, (300, 300))
    cv2.imshow('Control', img)

    retun, img = cv2.threshold(img, get_value.value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Image", img)

    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()
