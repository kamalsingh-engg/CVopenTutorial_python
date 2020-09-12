import cv2
import numpy as np
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
face_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
while True:
    ret, frame = cam.read()
    gray_img =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.05, minNeighbors=5)
    print(type(faces))
    print(faces)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)

    cv2.imshow("gray", img)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()