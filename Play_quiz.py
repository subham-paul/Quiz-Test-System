import importlib
flag=[0,0,0,0]
while True:
    print("\t-----------------------------")
    print("\t*** Users' Subject Choice ***")
    print("\t-----------------------------")
    print("1. PYTHON")
    print("2. JAVA")
    print("3. C")
    print("4. BACK TO YOUR PROFILE")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        if flag[0]==0:
            import Python_quiz     
            flag[0]=1
        else:
            importlib.reload(Python_quiz )
    elif choice==2:
        if flag[1]==0:
            import Java_quiz           
            flag[1]=1
        else:
            importlib.reload(Java_quiz)
    elif choice==3:
        if flag[2]==0:
            import C_quiz                 
            flag[2]=1
        else:
            importlib.reload(C_quiz)
    elif choice==4:
        if flag[3]==0:
            import USER                 
            flag[3]=1
        else:
            importlib.reload(USER)        
    elif choice==5:
        print("OK...")
        exit()
    else:
        print("Invalid Choice...Try Again!!!")


    
