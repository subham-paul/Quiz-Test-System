#import the module for database connection with mysql
import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='',host='localhost',database='quiz')

# prepare a cursor object using cursor() method
cursor = db.cursor()

#Accept user input
Uname=input('Enter user email to block::')

# Prepare SQL query to INSERT a record into the database.
sql = "Update login Set Status=0 WHERE Uname='%s'" % (Uname)

try:
    # Execute the SQL command
    cursor.execute(sql)
    
    if(cursor.rowcount==1):
        # Commit your changes in the database
        db.commit()
        print('Blocked Successfully...')
    else:
        # Rollback in case there is any error
        db.rollback()
        print('Status not Updated!!!')
except:
    # Rollback in case there is any error
    db.rollback()
    print('Status not Updated')

# disconnect from server
db.close()

