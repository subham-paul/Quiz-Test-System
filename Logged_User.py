import mysql.connector
# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM login"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    print("*************************LOGGED USER***************************")
    print("\n\n---------------------------------------------------------------")
    print("USERNAME\t\tFULL NAME\tMOBILE NO.\tSTATUS")
    print("---------------------------------------------------------------")
    for row in results:
        Uname = row[0]
        Fname = row[2]
        Mob = row[3]
        Status=row[4]
        # Now print fetched result
        print("\n%s\t%s\t%s\t%d" % \
        (Uname,Fname,Mob,Status))
except:
    print("Error: Unable to fecth data!!!")
# disconnect from server
db.close()
