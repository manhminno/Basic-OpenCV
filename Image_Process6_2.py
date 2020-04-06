import cv2
import matplotlib.pyplot as plt 
import numpy as np 

img = cv2.imread('image/himym.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5))/25
img2 = cv2.filter2D(img, -11, kernel)

matrix_sharpening = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
img3 = cv2.filter2D(img, -1, matrix_kenel)

plt.subplot(131)
plt.imshow(img)

plt.subplot(132)
plt.imshow(img2)

plt.subplot(133)
plt.imshow(img3)

plt.show()