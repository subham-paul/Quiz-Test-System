import mysql.connector
import datetime  
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
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
sql = "SELECT * FROM RESULT"
# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print("\n\n\t\t\t\t-:YOUR STATUS:-         ")
    print("\t\t\t------------------------------")
    for row in results:
        SL_NO = row[0]                            
        Uname = row[1]
        DOE=row[2]
        Sub= row[3]
        C_Ans = row[4]
        Marks = row[5]
        
        # Now print fetched result
        print("\n\nSL NO:: %d\nUSERNAME:: %s\nDATE OF EXAM:: %s\nSUBJECT:: %s\nCORRECT ANSWER:: %d\nMARKS:: %d" %(SL_NO, Uname,DOE, Sub, C_Ans, Marks))
    
        
except:
    print("Error: unable to fecth data")
cursor.close()

db.close()
    
