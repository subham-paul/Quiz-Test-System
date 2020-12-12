import importlib
flag=[0,0,0]
while True:
    print("\t----------------------------")
    print("\t****** Subject Choice ******")
    print("\t----------------------------")
    print("1. PYTHON")
    print("2. JAVA")
    print("3. BACK TO YOUR PROFILE")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        if flag[0]==0:
            import Python_Set     
            flag[0]=1
        else:
            importlib.reload(Python_Set )
    elif choice==2:
        if flag[1]==0:
            import Java_Set           
            flag[1]=1
        else:
            importlib.reload(Java_Set)    
    elif choice==3:
        if flag[2]==0:
            import ADMIN                 
            flag[2]=1
        else:
            importlib.reload(ADMIN)        
    elif choice==4:
        print("OK..")
        exit()
    else:
        print("Invalid Choice...Try Again!!!")


    
