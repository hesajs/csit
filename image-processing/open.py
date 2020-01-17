import numpy as np
import cv2

img = cv2.imread('naruto.jpg')
cv2.imshow('image', img)
img1 = cv2.imread('naruto.jpg', 0)
cv2.imshow('g', img1)
cv2.waitKey(0)
cv2.destoryAllWindows()
print(img.shape)
print(img[:, :, 0])
