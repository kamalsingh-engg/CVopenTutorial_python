import cv2
import numpy as np

def nothing(X):
    pass
cv2.namedWindow("tracking")
cv2.createTrackbar("LH","tracking",0,255,nothing)
cv2.createTrackbar("LS","tracking",0,255,nothing)
cv2.createTrackbar("LV","tracking",0,255,nothing)
cv2.createTrackbar("UH","tracking",255,255,nothing)
cv2.createTrackbar("US","tracking",255,255,nothing)
cv2.createTrackbar("UV","tracking",255,255,nothing)
while True:

    img = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    LH = cv2.getTrackbarPos("LH","tracking")
    LS = cv2.getTrackbarPos("LS", "tracking")
    LV = cv2.getTrackbarPos("LV", "tracking")
    UH = cv2.getTrackbarPos("UH", "tracking")
    US = cv2.getTrackbarPos("US", "tracking")
    UV = cv2.getTrackbarPos("UV", "tracking")
    l_b = np.array([LH,LS,LV])

    u_b =np.array([UH,US,UV])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('image',img)
    cv2.imshow('mask', mask)
    cv2.imshow('result',res)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()