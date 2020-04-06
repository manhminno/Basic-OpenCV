import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('image/image1(1).jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img)

for i in range(h.shape[0]):
    for j in range(h.shape[1]):
        if h[i][j] > 200:
            h[i][j] = 0

img = cv2.merge((h, s, v))
# cv2.imshow('Image', img)
# cv2.waitKey()
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
# plt.hist(h.ravel(), 256, (0, 256))
plt.show()