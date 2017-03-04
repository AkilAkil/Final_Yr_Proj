import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("onlinetoll24@gmail.com", "Gmail@123")
def sen(ma,tn):
    msg = "Hii!....Welcome,\nYour Vehicle: %s \n Thank You Visit again\n Have a safe Journey" % (tn)
    server.sendmail("onlinetoll24@gmail.com", ma, msg)
    server.quit()
