import importlib
flag=[0,0,0,0,0]
while True:
    print("\n\t-------------------")
    print("\t*** QUESTION SETUP ***")
    print("\t-------------------")
    print("1:INSERT NEW QUESTION")
    print("2:UPDATE QUESTION")
    print("3:DELETE QUESTION")
    print("4:Back")
    print("5:Exit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        if flag[0]==0:
            import INSERT_QUESTION           
            flag[0]=1
        else:
            importlib.reload(INSERT_QUESTION)
    if choice==2:
        if flag[1]==0:
            import Update_Question           
            flag[1]=1
        else:
            importlib.reload(Update_Question )
    elif choice==3:
        if flag[2]==0:
            import DELETE_QUESTION              
            flag[2]=1
        else:
            importlib.reload(DELETE_QUESTION)
    elif choice==4:
        if flag[3]==0:
            import ADMIN              
            flag[3]=1
        else:
            importlib.reload(ADMIN)        
    elif choice==5:
        print("OK...")
        exit()
    else:
        print("Invalid Choice...Try Again!!!")     
    

