import cv2
import numpy as np


img = cv2.imread('image/chessboard.jpg')
img2 = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.float32(img)

#Phat hien corner:
img = cv2.cornerHarris(img, 2, 3, 0.04)
img = cv2.dilate(img, None)

#Tim goc, va ve lai tren anh goc
# img > 0.01 x img.max() tim ra toa do goc
img2[img > 0.01*img.max()] = [0, 0, 255]

cv2.imshow('Img', img2)
cv2.waitKey() == ord('q')