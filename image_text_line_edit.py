import cv2
import numpy as np

img =cv2.imread('lena.jpg',1)
img = cv2.line(img,(0,0),(255,255),(255,0,0),10)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0), 10)
img = cv2.rectangle(img,(310,0),(510,150),(120,120,120), 5)
img = cv2.circle(img,(400,200),50,(0,0,120),4)
front = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'she is queen',(10,500),front,2,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)