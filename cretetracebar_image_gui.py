import numpy as np
import cv2
def nothing(x):
    print(x)


img= np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('b','image',0,255,nothing)
cv2.createTrackbar('g','image',0,255,nothing)
cv2.createTrackbar('r','image',0,255,nothing)
switch1 = '0: off\n 1:on'
cv2.createTrackbar(switch1,'image',0,1,nothing)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1) == 27:
        break
    b = cv2.getTrackbarPos('b','image')
    g = cv2.getTrackbarPos('g','image')
    r = cv2.getTrackbarPos('r','image')
    s = cv2.getTrackbarPos(switch1,'image')
    if s == 0:
        img[:]=0
    else:
        img[:]=[b,g,r]


cv2.destroyAllWindows()
