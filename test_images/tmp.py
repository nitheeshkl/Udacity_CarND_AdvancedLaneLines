from matplotlib import pyplot as plt
from matplotlib import image as mpimage
import cv2

img = cv2.imread('./test2.jpg')
plt.figure()
plt.imshow(img)
plt.show()
