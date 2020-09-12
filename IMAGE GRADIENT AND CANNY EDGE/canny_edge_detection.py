import cv2
import numpy as np
from matplotlib import pyplot as plt
#img = cv2.imread('messi5.jpg',0)
img = cv2.imread('lena.jpg',1)
edge = cv2.Canny(img,100,200)


title=['images','Canny Edge']
img = [img,edge]

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(img[i] , 'gray')# result can be check by only checking the image z0oming
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()