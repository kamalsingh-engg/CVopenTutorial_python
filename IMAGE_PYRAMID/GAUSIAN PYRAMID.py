import cv2
import numpy as np
from matplotlib import pyplot as plt
#img = cv2.imread('messi5.jpg',0)
img = cv2.imread('lena.jpg',1)
LR1 = cv2.pyrDown(img)
LR2 = cv2.pyrDown(LR1)
LR3 = cv2.pyrDown(LR2)
HR1 = cv2.pyrUp(LR3)

cv2.imshow('img',img)
cv2.imshow('LR1',LR1)
cv2.imshow('LR2',LR2)
cv2.imshow('LR3',LR3)
cv2.imshow('LR4',HR1)
cv2.waitKey(0)
cv2.destroyAllWindows()