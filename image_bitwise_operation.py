import numpy as np
import cv2
img= np.zeros((512,512,3),np.uint8)
img1= np.zeros((512,512,3),np.uint8)
img=cv2.rectangle(img,(200,0),(300,150),(255,255,255),-1)
img1=cv2.rectangle(img1,(200,372),(300,512),(255,255,255),-1)
cv2.imshow('image',img)
cv2.imshow('image1',img1)

#img3 = cv2.bitwise_and(img,img1)
#img4 = cv2.bitwise_or(img,img1)
img5 = cv2.bitwise_not(img)
#img6 = cv2.bitwise_xor(img,img1)
#cv2.imshow('image3',img3)
#cv2.imshow('image4',img4)
cv2.imshow('image5',img5)
#cv2.imshow('image6',img6)
cv2.waitKey(0)
cv2.destroyAllWindows()