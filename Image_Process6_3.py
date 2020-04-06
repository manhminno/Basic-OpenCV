import numpy as np 
import matplotlib as plt  
import cv2 

img = cv2.imread('image/deer_salt.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.medianBlur(img, 3)

cv2.imshow('Image', img)
# cv2.waitKey() == ord('q')

# img = cv2.imread('image/moon_dark.jpg')

# img = cv2.medianBlur(img, 3)
# matrix_sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# img = cv2.filter2D(img, -1, matrix_sharpen)
# img = cv2.convertScaleAbs(img, -1, 5) # dung` khi anh phan biet ro ret trang den, hoac sang anh

# cv2.imshow('Image', img)
# cv2.waitKey () == ord('q')

# img = cv2.imread('image/balloon.jpg')
# img = cv2.equalizeHist(img)

# cv2.imshow('Image', img)
# cv2.waitKey () == ord('q')

# img = cv2.imread('image/girl2_dark.jpg', cv2.IMREAD_COLOR)

# h, s, v = cv2.split(img)
# v = cv2.equalizeHist(v)
# img = cv2.merge((h, s, v))
# img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

#neu dung plt.imshow thi anh se tra ve dang BGR con cv2.imshow thi la RGB
# cv2.imshow('Image', img)
cv2.waitKey () == ord('q')

#medianBlur -> Khu nhieu hat nho, nhieu`
#can bang his-> lam ro chi tiet, neu bi phu 1 lop layer mo`
#convertScaleAbs -> neu anh toi' deu`
#GaussianBlur -> Khu nhieu lam mo tong the