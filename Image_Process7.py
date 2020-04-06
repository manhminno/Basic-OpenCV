#Threshsold: cv2.threshsold binayry: nho hon nguong thi = 0, neu k thi bang chi so sau
import numpy as np 
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('data/0/CL61_S2.png', cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (9, 9), 0)

#sobel
sobelx64f = cv2.Sobel(img_blur,cv2.CV_64F, 1, 0, 3)
abs_sobel64f = np.abs(sobelx64f)
img_sobelx = np.uint8(abs_sobel64f)

sobely64f = cv2.Sobel(img_blur,cv2.CV_64F, 1, 0, 3)
abs_sobel64f = np.abs(sobely64f)
img_sobely = np.uint8(abs_sobel64f)

img_sobel = (img_sobelx + img_sobely)/2

ret, img_sobel = cv2.threshold(img_sobel, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Sobel', img_sobel)


img2 = cv2.imread('data/0/CL61_S2.png', cv2.IMREAD_GRAYSCALE)
img2_blur = cv2.GaussianBlur(img2, (5, 5), 0)

# Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img2_blur, -1, kernelx)
img_prewitty = cv2.filter2D(img2_blur, -1, kernely)
img_prewitt1 = (img_prewittx + img_prewitty)/2

ret, img_prewitt = cv2.threshold(img_sobel, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Prewitt', img_prewitt)


img3 = cv2.imread('data/0/CL61_S2.png', cv2.IMREAD_GRAYSCALE)
img3_blur = cv2.GaussianBlur(img2, (5, 5), 0)
img_canny = cv2.Canny(img3_blur, 30, 255)

# ret, img_canny = cv2.threshold(img_canny, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Canny', img_canny)
cv2.waitKey() == ord('q')

#sobel
#prewitt
#canny -> pho bien cho duong` bien nho -> dung dao ham bac 2 -> k can dung threshold nua