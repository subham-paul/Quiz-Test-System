# Feedback.py
import mysql.connector
import datetime         #For System DateTime
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
Uname=""
f=open("login.txt","r")
Uname=f.readline()
f.close()

print("---------------------------------------")
print("           FEEDBACK FORM            ")
print("---------------------------------------") 
MSG=input("\n\nEnter the Message:")
now = datetime.datetime.now()
datetime_str=now.strftime("%Y-%m-%d %H:%M:%S")

# Coding to Save the Feedback details at Feedback Table
sql = "INSERT INTO feedback(Uname,MSG,F_Date) \
VALUES ('%s', '%s', '%s')" % \
(Uname,MSG,datetime_str)
cursor = db.cursor()
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Feedback Recorded Successfully...')
    print('\n\n**********THANK YOU************')
    New=input("\n\t\t BACK TO SUBJECT CHOICE <<<(Type Y/N)>>>")
    if New =='Y' or New =='y':
        import USER
    else:
        print("Exit...")
        exit()
except:
    # Rollback in case there is any error
    db.rollback()
    print('Feedback not saved. Check Primary Key and other fields.')

