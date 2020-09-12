import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
gradient = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)


title=['images','mask','dilation','erosion','opening','closing','gradient','th']
img = [img,mask,dilation,erosion,opening,closing,gradient,th]

for i in range(8):
    plt.subplot(3,3,i+1), plt.imshow(img[i] , 'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()