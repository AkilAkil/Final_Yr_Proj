import numpy as np
import cv2
import time
import log
num_plate__cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cap = cv2.VideoCapture('Car.mp4')
time.sleep(2)
k=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = num_plate__cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        crp = img[y:y+h, x:x+w]
        cv2.imwrite("img4.jpg",crp)
	from PIL import Image
	import pytesseract
	i=Image.open("img4.jpg")
	j = pytesseract.image_to_string(i)
    print j
    log.store(j,k)
    k +=1
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break;

cap.release()
cv2.destroyAllWindows()
