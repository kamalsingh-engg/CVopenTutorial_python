import cv2
cap = cv2.VideoCapture(0)  #default webcam
# we can use the command like for while condition is cap.isOpened()
print(cap.isOpened())
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
