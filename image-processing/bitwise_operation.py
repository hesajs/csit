import cv2
import numpy as np

img = cv2.imread('brect.png')
img = cv2.resize(img, (256, 256))
img_1 = cv2.bitwise_not(img, mask=None)
cv2.imshow('Bitwise', img)
cv2.imshow('Bitwise Not', img_1)
img_2 = cv2.imread('bcircle.png')
img_2 = cv2.resize(img, (256, 256))
dest_and = cv2.bitwise_and(img_2, img_1, mask=None)

cv2.imshow('Bitwise And', dest_and)
cv2.waitKey(0)
cv2.destroyallWindows()