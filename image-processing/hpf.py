import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('naruto.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
#

fshift[crow-30: crow+30, ccol-30, ccol+30]
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift) Q
img_back = np.abs(img_back)
plt.subplot(231), plt.imshow(img_back, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('low pass filter'), plt.xticks([]), plt.yticks([])
plt.show()