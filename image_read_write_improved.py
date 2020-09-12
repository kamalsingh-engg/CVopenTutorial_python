import cv2
#image read function
img = cv2.imread('image1.jpg',-1)
print(img)
#img = cv2.imread('image1.jpg',1) this is for the rgb color

#img = cv2.imread('image1.jpg',-1) this is for the original color
cv2.imshow('image',img)
k = cv2.waitKey(0) #it is wait for the 5 sec if 0 then it will only close by close the windows
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('image2_copy.png',img)
    cv2.destroyAllWindows()
