import cv2
import numpy as np
import datetime
import os
from datetime import datetime,timedelta
from time import sleep
cap = cv2.VideoCapture(0)


k=0
while cap.isOpened():

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    now = datetime.now()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations = 3)
    #cv2.imshow('inter',frame1)

    save_path = 'D:/python_iot1/kamal/'
    filename = 'motion{}_{}'.format(now.minute,now.second)
    completename = os.path.join(save_path, filename + '.jpg')
    #completename = 'motion{}_{}.jpg'.format(now.minute,now.second)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #cv2.imwrite(completename, frame1)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue

        cv2.imwrite(completename, frame1)
        #sleep(0.01)



        #cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, 'status: {}'.format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    #cv2.drawContours(frame1, contours, -1,(0,255,0),2)

    cv2.imshow('feed', frame1)
    frame1=frame2
    ret,frame2 = cap.read()




    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()