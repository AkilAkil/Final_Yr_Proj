import numpy as np
import cv2
import time
face_cascade = cv2.CascadeClassifier('cars.xml')
#eye_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture('/home/akil/Downloads/Proj/Car.mp4')
time.sleep(2)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
	crp = img[y:y+h, x:x+w]
	median = cv2.medianBlur(crp,5)
	cv2.imwrite("img1.jpg",median)
        

    cv2.imshow('Vid',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
