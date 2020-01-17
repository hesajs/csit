import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("shrapen-eye.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
gauss_mask = cv2.GaussianBlur(image, (9,9), 10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)
cv2.imshow("Output : Sharpen", image_sharp)
#High pass kernel 3x3
kernel = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1,-1]])
#image_hpf = image - gauss_mask
image_hpf = cv2.filter2D(image, -1, kernel)
cv2.imshow("Output : High Pass Filter", image_hpf)
cv2.waitKey(0)
