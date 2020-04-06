import numpy as np 
import cv2 


img = cv2.imread('image/house.jpg')
img2 = img.copy()

#phat hien goc:
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.float32(img)
img = cv2.cornerHarris(img, 2, 3, 0.04)
img = cv2.dilate(img, None)

#tim ra goc that tren anh goc:
img2[img > 0.01*img.max()] = [0, 0, 255]

cv2.imshow('Imgae', img2)
cv2.waitKey() == ord('q')