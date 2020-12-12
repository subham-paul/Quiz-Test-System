import random

#import the module for email
import smtplib
from email.mime.text import MIMEText

#import the module for database connection with mysql
import mysql.connector
import importlib

# Open database connection
db = mysql.connector.connect(user='root', password='',host='localhost',database='quiz')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Set the variables for email the OTP
smtp_ssl_host = 'smtp.gmail.com'        
smtp_ssl_port = 465
username = '------USER MAIL-ID------'   
password = '------USER PASSWORD------'           
sender = '------SENDER MAIL-ID------'     
otp = 0

# Function to send and validate the OTP
def email_OTP(usr):
    ok = 0
    targets = usr
    global otp
    otp = random.randint(10001,99999)
    msg = MIMEText('Your OTP for email ID Verification is: %d' % (otp))
    msg['Subject'] = 'OTP for Confirmation of User Registration'
    msg['From'] = sender
    msg['To'] = ''.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    try:
        server.sendmail(sender, targets, msg.as_string())
        ok = 1
        print('Email send successfully...')
    except:
        print('Invalid email-ID...Try again.')
        ok = 0
    server.quit()
    return ok

print('Register New user:~')
flag=0
while True:
    Uname=input('\n\nEnter Username [Email-ID]=')
    sql1="SELECT COUNT(*) FROM login WHERE Uname='%s'" % (Uname)
    try:
        cursor.execute(sql1)
        results=cursor.fetchall()
        for row in results:
            NO=row[0]
        if NO==0:
            print('Username is accepted.Now you get an otp in your email to verify your Email-ID...')
            chk=email_OTP(Uname)
            if chk==1:
                break
        else:
            print('Username already registered,Please try another or login ...')
            import SIGNIN
    except:
        print("Access Error")


while True:
    confirm_otp=int(input('Enter the OTP that you receive:'))
    print("OTP sent as %d and you type %d" % (otp,confirm_otp))
    if(otp==confirm_otp):
        break
    else:
        print('OTP not matched Try Again!!!')        
   
Fname=input('ENTER YOUR FULL NAME::')
Pwd=input('ENTER NEW PASSWORD::')
Mob=input('ENTER YOUR MOBILE NUMBER::')


# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO LOGIN(Uname,Fname,Pwd,Mob,Status) \
VALUES ('%s','%s','%s','%s',1)" % \
(Uname,Fname,Pwd,Mob)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Sign Up  successfully...')
    if flag==0:
        flag=1
        import SIGNIN               
    else:
        importlib.reload(SIGNIN)
except:
    # Rollback in case there is any error
    db.rollback()
    print('something error.')   

# disconnect from server
db.close()
