import mysql.connector
import datetime         #For System DateTime
import sys  
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM question WHERE Sub='PYTHON'"

ans=[0,0,0,0]
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print("---------------------------------------")
    print("                PYTHON SET     ")
    print("---------------------------------------")      
    for row in results:
         Sub=row[1]
         Qno= row[0]
         Qstn=row[2]
         o1=row[3]
         o2=row[4]
         o3=row[5]
         o4=row[6]
         Ans=row[7]
         
        # Now print fetched result
    
         print("\n\n%d%s\n%s\t%s\t%s\t%s\t%s" % \
         (Qno,Qstn,o1,o2,o3,o4,Ans))
    New=input("\n\t\t BACK TO SUBJECT CHOICE <<<(Type Y/N)>>>")
    if New =='Y' or New=='y':
        import Question_Set_Details
    else:
        print("Exit...")
        exit()
except:
    print("Something Error....")
# disconnect from server
cursor.close()

