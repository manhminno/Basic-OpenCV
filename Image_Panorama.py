import numpy as np 
import cv2 


#Pano1
img = cv2.imread('image/panorama/mountain1_left.png')
img2 = cv2.imread('image/panorama/mountain1_right.png')

#Pano2
img1 = cv2.imread('image/panorama/scottsdale_left.png')
img12 = cv2.imread('image/panorama/scottsdale_right.png')

#Ghep panorama:
stitcher = cv2.createStitcher(True)
result = stitcher.stitch((img, img2))
rs2 = stitcher.stitch((img1, img12))


cv2.imshow('Img', result[1])
cv2.imshow('Rs2', rs2[1])
cv2.waitKey() == ord('q')