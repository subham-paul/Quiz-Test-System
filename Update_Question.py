# Update records
#import the module for database connection with mysql
import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='',host='localhost',database='quiz')

# prepare a cursor object using cursor() method
cursor = db.cursor()
print("---------------------------------------")
print("           UPDATE QUESTION SET            ")
print("---------------------------------------") 
#Accept user input
Qno=int(input('Enter Qno. to update details='))
Sub=input("Enter New Subject::")
Qstn=input('Enter New question::')
OP1=input('Enter option1::')
OP2=input('Enter option2::')
OP3=input('Enter option3::')
OP4=input('Enter option4::')
Ans=input('Enter Answer::')
C=int(input("Enter correct answer::"))   
   
# Prepare SQL query to INSERT a record into the database.
sql = "UPDATE question SET Sub='%s',Qstn='%s',Option1='%s',Option2='%s',Option3='%s',Option4='%s',Ans='%s',C_ANS='%d' \
WHERE Qno='%d'" % \
(Sub,Qstn,OP1,OP2,OP3,OP4,Ans,C,Qno)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Question Updaed Successfully...')
    s=input("Do you want to update any question again? [Y/N]::")
    if s!='Y' and s!='y':
        import Edit_Question
    else:
        import Update_Question

except:
    # Rollback in case there is any error
    db.rollback()
    print('Question not Updated!!!')

# disconnect from server
db.close()
