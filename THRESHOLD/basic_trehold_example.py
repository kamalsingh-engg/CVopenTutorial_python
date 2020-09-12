import cv2
import numpy as np

img = cv2.imread("gradient.png",0)

_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th6 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
_,th7 = cv2.threshold(img,127,255,cv2.THRESH_MASK)
cv2.imshow('image',img)
cv2.imshow('TH1',th1)
cv2.imshow('TH2', th2)
cv2.imshow('TH3', th3)
cv2.imshow('TH4', th4)
cv2.imshow('TH5', th5)
cv2.imshow('TH6', th6)
cv2.imshow('TH7', th7)
cv2.waitKey(0)
cv2.destroyAllWindows()