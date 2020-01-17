import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('dark-img.jpg', 0)
img2 = cv2.imread('low-contjpg', 0)
img3 = cv2.imread('xray.jpeg', 0)

histr = cv2.calcHist([img1], [0], None, [256], [0, 256])
histr2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
histr3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img1), plt.title('DARK')
plt.subplot(222), plt.plot(histr, 'red'), plt.title('DARK')
plt.subplot(223), plt.imshow(img3), plt.title('LIGHT')
plt.subplot(224), plt.plot(histr3, 'blue'), plt.title('LIGHT')

# plt.plot(histr)
# plt.plot(histr2)
# plt.plot(histr3)
plt.show()


plt.show()