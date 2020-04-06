from skimage.feature import hog
import numpy as np 
import cv2
import skimage

img = cv2.imread('image/man.png')

#hog:
fd, hog_img = hog(img, 9, (8, 8), (1, 1), visualize=True)

#rescale cho display
hog_img = skimage.exposure.rescale_intensity(hog_img, (0, 10))

print(fd.shape)

cv2.imshow('Img', hog_img)
cv2.waitKey() == ord('q')