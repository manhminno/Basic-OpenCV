import numpy as np 
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('image/lane1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image/lane2.png', cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (5, 5), 0)
img2 = cv2.GaussianBlur(img2, (5, 5), 0)

#Detec bien
img = cv2.Canny(img, 30, 255)
img2 = cv2.Canny(img2, 30, 255)

#Hough Lines
lines = cv2.HoughLinesP(img, 1, np.pi/180, 50)

N = lines.shape[0]
for i in range(N):
    x1 = lines[i][0][0]
    y1 = lines[i][0][1]    
    x2 = lines[i][0][2]
    y2 = lines[i][0][3]    
    cv2.line(img,(x1,y1),(x2,y2),(255, 0, 0), 2)


cv2.imshow('Image', img)
cv2.imshow('Image2', img2)
cv2.waitKey() == ord('q')