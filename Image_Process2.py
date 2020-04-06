import numpy as np 
import cv2
import matplotlib.pyplot as plt 

img = np.empty((600, 800 , 3))
img[:, :, [0, 1, 2]] = 255 #White
# img[:, :, [1]] = 255 #Green
# img[:, :, [2]] = 255 #Blue

cv2.line(img, (200, 300), (100, 100), (0, 0, 0)) #Line noi 2 diem toa do
for i in range(0, 600, 50):
    cv2.line(img, (0, i), (5, i), (0, 0, 0))
cv2.circle(img, (100, 100), 100, (255, 0, 0))
cv2.ellipse(img, (300, 300), (100, 50), 45, 0, 360, (0,255,0))
pts = np.array(((10,  0), (100, 100), (200, 500), (300, 600)), np.int32)
pts = [pts.reshape((4, 1, 2))]
cv2.polylines(img, pts, True, (0, 0, 0))

plt.imshow(img)
plt.show()
