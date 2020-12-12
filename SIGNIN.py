# Login.py
import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='quiz')

# prepare a cursor object using cursor() method
cursor = db.cursor()
try:
    print('\n\t\t~:LOGIN PAGE:~')
    New=input("\n\t\t ARE YOU NEW USER??? <<<(Type Y/N)>>>")
    if New =='Y' or New=='y':
        import SIGNUP
    if New =='N' or New=='n':
        U=input("\nEnter the Username [Email-ID]=")
        Pwd=input("Enter the Password=")
except:
    print('Invalid data!!!')
    db.close()
    exit()

# Prepare SQL query MySQL Table Names under the User.
sql = "SELECT * FROM login WHERE Uname='%s' AND Pwd='%s' AND Status=1" % (U,Pwd)

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()    
    for row in results:
        Uname = row[0]
        Pwd = row[1]
        Fname = row[2]
        Mob = row[3]
        Status=row[4]
        # Now print fetched result        
        print("\n\nWelcome %s to UNIQUE LEARNING..." % \
        (Fname))
        # Write the username to the LoggedUser.txt
        f=open("Login.txt","w")
        f.write(Uname)
        f.close()
    if Uname=="suman@aptechkolkata.com":
        import ADMIN    
    else:
        import USER
    if Uname:
        print('')
except:
    print("Error: Invalid Username or Password or you are blocked!!!")
    exit()
# disconnect from server
cursor.close()
db.close()
