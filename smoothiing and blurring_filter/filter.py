import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv-logo.png') 
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernal = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernal)
blurr = cv2.blur(img,(5,5))
gf = cv2.GaussianBlur(img,(5,5),0)

title=['images','2D-convolution','blurr','gaussian Filter']
img = [img,dst,blurr,gf]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(img[i] , 'gray')# result can be check by only checking the image z0oming
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()