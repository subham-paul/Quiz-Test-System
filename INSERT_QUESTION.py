#import the module for database connection with mysql
import mysql.connector
# Open database connection
db = mysql.connector.connect(user='root', password='',host='localhost',database='quiz')
#print('Connection ok...')

# prepare a cursor object using cursor() method
cursor = db.cursor()
print("---------------------------------------")
print("           NEW QUESTION ENTRY            ")
print("---------------------------------------") 
#Accept user input
Qno=int(input('Enter new Qno. to insert::'))
Sub=input("Enter New Subject::")
Qstn=input('Enter New question::')
OP1=input('Enter option1::')
OP2=input('Enter option2::')
OP3=input('Enter option3::')
OP4=input('Enter option4::')
Ans=input('Enter Answer with Explanation::')
C=int(input("Enter correct answer number [1/2/3/4]::"))

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO QUESTION(Qno,Sub,Qstn,Option1,Option2,Option3,Option4,Ans,C_ANS) \
VALUES ('%d','%s', '%s','%s','%s','%s','%s','%s','%d')" % \
(Qno,Sub,Qstn,OP1,OP2,OP3,OP4,Ans,C)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Question Inserted successfully...')
    s=input("Do you want to insert new question again? [Y/N]::")
    if s!='Y' and s!='y':
        import Edit_Question
    else:
        import INSERT_QUESTION
except:
    # Rollback in case there is any error
    db.rollback()
    print('Question not saved. Check Primary Key and other fields.')

# disconnect from server
cursor.close()
db.close()
