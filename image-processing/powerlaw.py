import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fade.jpg', 0)
img_1 = cv2.resize(img, (256, 256))
gamma = 1.25
img_2 = np.power(img_1, gamma)
gamma = 1.5 
img_3 = np.power(img_1, gamma)
gamma = 1.75 
img_4 = np.power(img_1, gamma)

cv2.imshow('input_image', img_1)
cv2.imshow('gamma 2', img_2)
cv2.imshow('gamma 3', img_3)
cv2.imshow('gamma 4', img_4)
cv2.waitKey(1000000)
cv2.destroyallWindows()