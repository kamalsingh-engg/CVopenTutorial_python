import cv2
#image read function
img = cv2.imread('image1.jpg',1)
print(img)
#img = cv2.imread('image1.jpg',1) this is for the rgb color

#img = cv2.imread('image1.jpg',-1) this is for the original color
cv2.imshow('image',img)
cv2.waitKey(5000) #it is wait for the 5 sec if 0 then it will only close by close the windows
cv2.destroyAllWindows()
#image write
cv2.imwrite('image1_copy.png',img)
