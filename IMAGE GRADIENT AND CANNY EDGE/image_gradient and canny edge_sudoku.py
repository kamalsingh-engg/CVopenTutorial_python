import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobelY))
com_res = cv2.bitwise_or(sobelx,sobely)



title=['images','laplacian ','sobelx','sobely','combuned result']
img = [img,lap,sobelx,sobely,com_res]

for i in range(5):
    plt.subplot(3,2,i+1), plt.imshow(img[i] , 'gray')# result can be check by only checking the image z0oming
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()