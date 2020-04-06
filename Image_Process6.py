import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('image/image2.jpeg')
# cv2.imshow("Image", img)
# cv2.waitKey()
# img[:,:,:] += 100
plt.subplot(211)
plt.imshow(img)

# plt.subplot(412)
# plt.hist(img.ravel(),256, [0,256])

# equ = cv2.equalizeHist(img[:, :, [0]])
# equ = cv2.equalizeHist(img[:, :, [1]])
# equ = cv2.equalizeHist(img[:, :, [2]])
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(128, 128))
equ = clahe.apply(img[:, :, [0]])
equ = clahe.apply(img[:, :, [1]])
equ = clahe.apply(img[:, :, [2]])
plt.subplot(212)
plt.imshow(equ)

# plt.subplot(414)
# plt.hist(equ.ravel(),256, [0,256])

plt.show()