import numpy as np
import cv2
img = cv2.imread('messi5.jpg',1)
img2= cv2.imread('opencv-logo.png',1)
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

#print(img.shape)
#print(img.size)
#print(img.dtype)
#b,g,r=cv2.split(img)
#img = cv2.merge((b,g,r))
#img3=cv2.add(img,img2)
img3 = cv2.addWeighted(img,0.7,img2,0.3,0)
#ball = img[280:340,330:390]
#img[273:333,100:160] = ball
cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

