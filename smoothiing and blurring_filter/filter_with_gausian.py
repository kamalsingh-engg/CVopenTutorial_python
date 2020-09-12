import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('salt and paper noise.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernal = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernal)
blurr = cv2.blur(img,(5,5))
gf = cv2.GaussianBlur(img,(5,5),0)
mf= cv2.medianBlur(img,5)
bf = cv2.bilateralFilter(img,9,75,75)
title=['images','2D-convolution','blurr','gaussian Filter','median blur','bilateral filter']
img = [img,dst,blurr,gf,mf,bf]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(img[i] , 'gray')# result can be check by only checking the image z0oming
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()