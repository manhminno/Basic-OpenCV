import os
import numpy as np 
import cv2
import matplotlib
import matplotlib.pyplot as plt

list = []
path = os.listdir('image')

for i in range(len(path)):
    temp = os.path.join('image', path[i])
    list.append(temp)

# print(list)
# link = os.path.abspath('image')
# print(link)

img = cv2.imread(list[0])
# print(img.shape,'is', type(img))

# plt.imshow(img)
# plt.show()

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img2 = img[..., ::-1]
# img2 = img[..., ::-1]
# print(type(img2))
# print(img2.shape)
# img2 = cv2.resize(img2, (150, 150))
b_chanel = img2
b_chanel[:, :, [0, 1]] = 0

img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert color channel
plt.imshow(img3)
# plt.imshow(img2)
plt.show()