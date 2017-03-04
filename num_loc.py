import numpy as np
import cv2
import datetime
import MySQLdb
import time
import mail
import pytesseract
num_plate__cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cap = cv2.VideoCapture('ferrari.mpeg')
time.sleep(2)
db = MySQLdb.connect("localhost","root","1234","proj" )
cur=db.cursor()
sql1= "SELECT * FROM numplate"
num_pl=0
date_time_now=str(datetime.datetime.now())
dt = time.strftime("%Y-%m-%d")
tm = time.strftime("%H-%M")
print dt
print tm
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = num_plate__cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        crp = img[y:y+h, x:x+w]
        cv2.imwrite("img4.jpg",crp)
	from PIL import Image
	i=Image.open("img4.jpg")
	num_pl= pytesseract.image_to_string(i)         
    try:
        cur.execute(sql1)
        results = cur.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            if num_pl==fname:
                t1=(num_pl,)
                print "Match found : \nnum=%s,name=%s" % \
                (fname, lname,)              
                cur.execute("select date_nw from log where veh_num='%s'" % (num_pl))
                row=cur.fetchall()
                dtin=int(date_nw)
                print dtin
                if row==None or not row: 
                    cur.execute("INSERT INTO log(veh_num,date_nw,time_nw) VALUES (%s,%s,%s)",(fname,dt,tm))
                    db.commit()
                    mail.sen("dharanish185@gmail.com",fname)
                time.sleep(10)
            else:
                print "Does not match"
    except:
        print "error"
        time.sleep(5)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break;
cap.release()
cv2.destroyAllWindows()