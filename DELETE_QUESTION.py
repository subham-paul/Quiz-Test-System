# Delete records under the User root and Database quiz

#import the module for database connection with mysql
import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='',host='localhost',database='quiz')

# prepare a cursor object using cursor() method
cursor = db.cursor()
print("---------------------------------------")
print("           QUESTION DELETION            ")
print("---------------------------------------") 
#Accept user input
Qno=int(input('Enter Qno. to delete::'))

# Prepare SQL query to INSERT a record into the database.
sql = "DELETE FROM question WHERE Qno='%d'" % (Qno)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
    print('Question Deleted Successfully...')
    s=input("Do you want to delete question again? [Y/N]::")
    if s!='Y' and s!='y':
        import Edit_Question
    else:
        import DELETE_QUESTION
except:
    # Rollback in case there is any error
    db.rollback()
    print('Question not Deleted!!!')

# disconnect from server
db.close()
