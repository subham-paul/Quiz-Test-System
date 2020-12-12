import mysql.connector
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM feedback"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()    
    print("\t\t\t\t-:ALL FEEDBACK DETAILS:-")
    print("\t\t\t\t------------------------")
    print("FEEDBACKNO\tUSERNAME\t\tFEEDBACK_DATE\tMESSAGE")
    for row in results:
        SL_NO = row[0]
        Uname = row[1]
        F_Date = row[2]
        MSG = row[3]            
        
        # Now print fetched result
        print("%s\t%s\t%s\t%s" % \
        (SL_NO,Uname,F_Date,MSG))
    New=input("\n\t\t BACK TO YOUR PROFILE <<<(Type Y/N)>>>")
    if New =='Y' or New =='y':
        import ADMIN
    else:
        print("exit...")
        exit()
   
except:
    print("Error: unable to fecth data!!!")
# disconnect from server
db.close()
