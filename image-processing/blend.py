import cv2
import numpy as np

img1 = cv2.imread('naruto.jpg')
img2 = cv2.imread('btree.png')
print(img1.shape)
print(img2.shape)
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()