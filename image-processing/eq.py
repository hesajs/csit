import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('naruto.jpg', 0)
img_1 = cv2.resize(img, (256, 256))

equ = cv2.equalizeHist(img_1)
# res = np.hstack((img_1, equ))
# cv2.imshow('naruto.jpg', res)
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
histr2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img_1), plt.title('DARK')
plt.subplot(222), plt.plot(histr, 'red'), plt.title('DARK')
plt.subplot(223), plt.imshow(equ), plt.title('LIGHT')
plt.subplot(224), plt.plot(histr2, 'blue'), plt.title('LIGHT')

# cv2.waitKey(0)
# cv2.destoryAllWindows()