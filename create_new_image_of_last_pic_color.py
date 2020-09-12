import cv2
import numpy as np

def click_event(event,x,y,flag,param):

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        myimage = np.zeros((512,512,3),np.uint8)
        myimage[:] =[blue,green,red]
        cv2.imshow('color', myimage)


img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()