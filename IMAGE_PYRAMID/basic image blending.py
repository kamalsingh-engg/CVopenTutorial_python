import cv2
import numpy as np
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
orange_apple = np.hstack((apple[:,: 256],orange[:,256 :]))
cv2.imshow('orange&apple',orange_apple)

cv2.waitKey(0)
cv2.destroyAllWindows()