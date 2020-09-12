import cv2
cap = cv2.VideoCapture(0)  #default webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video1.mp4',fourcc,20,(640,480))
# we can use the command like for while condition is cap.isOpened()
print(cap.isOpened())
while True:
    ret, frame = cap.read()
    if ret == 1:
        out.write(frame)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', frame)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()

