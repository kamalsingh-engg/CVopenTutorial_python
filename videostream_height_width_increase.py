import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,500)
cap.set(4,500)
print(cap.get(3))
print(cap.get(4))

#default webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('video1.mp4',fourcc,20,(640,480))
# we can use the command like for while condition is cap.isOpened()
#print(cap.isOpened())
while True:
    ret, frame = cap.read()
    if ret == 1:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width:'+str(cap.get(3))+ 'height:'+str(cap.get(4))
        cv2.putText(frame,text,(10,30),font,1,(0,255,0),2,cv2.LINE_AA)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', frame)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

