import cv2
import numpy as np

img_1 = cv2.imread('btree.png',0)
# converting into integer data type
img_2 = np.uint8(np.log1p(img_1))

thresh = 1
img_3 = cv2.threshold(img_2, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('input image', img_1)
cv2.imshow('log transformed', img_3)
cv2.waitKey(100000000)
cv2.destroyallWindows()