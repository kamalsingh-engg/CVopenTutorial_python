import cv2
import numpy as np
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
#cv2.imshow('apple',apple)
#cv2.imshow('orange',orange)
orange_apple = np.hstack((apple[:,: 256],orange[:,256 :]))
#cv2.imshow('orange&apple',orange_apple)

#genrate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    #cv2.imshow('str(i)',layer)

#genrate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    #cv2.imshow('str(i)',layer)
#generate laplace pyramid for the gaussian pyramid of apple
apple_copy = gp_apple[5]
#cv2.imshow('the gaussian upper image',layer)
lp_apple = [apple_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)
#generate laplace pyramid for the gaussian pyramid of orange
orange_copy = gp_orange[5]
#cv2.imshow('the gaussian upper image',layer)
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)

#now add left and right part of the laplacian image

apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n += 1
    cols,rows,ch = apple_lap.shape
    laplacian =np.hstack((apple_lap[:,0:int(rows/2)],orange_lap[:,int(rows/2) :]))
    apple_orange_pyramid.append(laplacian)

#reconstruct the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple and orange',orange_apple)
cv2.imshow('apple and orange reconstruct',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()

