import mysql.connector
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    SL_NO=int(input("Enter serial number::") )
except:
    print('Invalid data!!!')
    db.close()
    exit()

# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM result WHERE SL_NO='%d'" % (SL_NO)
flag = 0
try: 
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()    
    print("\n\n\t\t\t-:User's STATUS:-")
    print("\t\t\t-----------------")
    for row in results:
        SL_NO=row[0] 
        Uname=row[1]
        DOE=row[2]
        Sub= row[3]
        C_Ans = row[4]
        Marks = row[5]

        flag=1
        
        # Now print fetched result
        print("\nUSERNAME:: %s\nDATE OF EXAM:: %s\nSUBJECT:: %s\nCORRECT ANSWER:: %d\nMARKS OUT OF 20:: %d" %(Uname,DOE, Sub, C_Ans, Marks))    

    if flag==0:
        print('\nError: Unable to fetch data!!!')
except:
    print("Error: unable to fetch data!!!")
# disconnect from server
cursor.close()
db.close()

