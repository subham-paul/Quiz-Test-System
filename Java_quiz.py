import mysql.connector
import datetime         #For System DateTime
import sys  
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM question WHERE Sub='JAVA'"

ans=0
count=0
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print("Start your exam now...\n")
    for row in results:
         Sub=row[1]
         Qno= row[0]
         Qstn=row[2]
         o1=row[3]
         o2=row[4]
         o3=row[5]
         o4=row[6]
         
         f=open("Sub.txt","w")
         f.write(Sub)
         f.close()
        # Now print fetched result
    
         print("\n\n%d%s\nChoose any one option:\n%s\n%s\n%s\n%s" % \
         (Qno,Qstn,o1,o2,o3,o4))
         ans=int(input('\nËnter your choice: Type 1/2/3/4 only:'))
         if ans==row[8]:
             count=count+1
             print('\nCorrect...')
         else:
             print("\nWrong")
             print("Correct Answer:\n%s" % row[7])                              
         
except:
    print("Error: Unable to fecth data!")
# disconnect from server
cursor.close()


cursor = db.cursor()
#Read the Username from Login.txt, Subject from sub.txt
Uname=""
f=open("login.txt","r")
Uname=f.readline()
f.close()
Sub=""
f1=open("Sub.txt","r")
Sub=f1.readline()
f1.close()
now = datetime.datetime.now()
datetime_str=now.strftime("%Y-%m-%d %H:%M:%S")


# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO result(Uname,Sub,DOE,C_Ans,Marks) \
VALUES ('%s', '%s', '%s', '%d', '%d')" % \
(Uname,Sub,datetime_str,count,count*5)
cursor = db.cursor()
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Result Recorded Successfully...')    
except:
     # Rollback in case there is any error
    db.rollback()
    print('Reecord not saved. Check Primary Key and other fields.')
cursor.close()

print("\n\t--:RESULT:--")
print("\nUSERNAME:: ",Uname)
print("SUBJECT:: ",Sub)
print("DATE OF EXAM:: ",datetime_str)
print("CORRECT ANSWER:: ",count)
print("TOTAL MARKS out of 20:: ",count*5)
print("\n\n\t\t---------------THANK YOU---------------")



cursor.close()
db.close()
    
