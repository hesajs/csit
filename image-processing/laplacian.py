import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)

imageWob = cv2.Laplacian(image, cv2.CV_64F, ksize=1)
cv2.imshow("Output : 2nd Ord Derivative w/o Blur", imageWob)

image = cv2.GaussianBlur(image, (3, 3), 5.0)
image = cv2.Laplacian(image, cv2.CV_64F, ksize=1)
cv2.imshow("Output : 2nd Ord Derivative", image)
cv2.waitKey(0)