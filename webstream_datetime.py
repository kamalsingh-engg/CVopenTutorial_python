import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3,1208)
#cap.set(4,724)
#print(cap.get(3))
#print(cap.get(4))

#default webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('video1.mp4',fourcc,20,(640,480))
# we can use the command like for while condition is cap.isOpened()
#print(cap.isOpened())
while True:
    ret, frame = cap.read()
    if ret == 1:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(datetime.datetime.now())
        cv2.putText(frame,text,(10,30),font,0.8,(0,0,255),4,cv2.LINE_AA)

        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

