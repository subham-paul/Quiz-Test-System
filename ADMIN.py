import importlib
flag=[0,0,0,0,0,0,0]
while True:
    print("\n\t-------------------")
    print("\t*** Admin Page ***")
    print("\t-------------------")
    print("1:All Logged User Details")
    print("2:Result Details of a User")
    print("3:Question Set Details")      
    print("4:Edit Question Set Up")
    print("5:Block user")
    print("6:Feedback record")
    print("7:Back")
    print("8:Exit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        if flag[0]==0:
            import Logged_User           
            flag[0]=1
        else:
            importlib.reload(Logged_User)
    elif choice==2:
        if flag[1]==0:
            import Users_Details            
            flag[1]=1
        else:
            importlib.reload(Users_Details)
    elif choice==3:
        if flag[2]==0:
            import Question_Set_Details               
            flag[2]=1
        else:
            importlib.reload(Question_Set_Details)
    elif choice==4:
        if flag[3]==0:
            import Edit_Question              
            flag[3]=1
        else:
            importlib.reload(Edit_Question)
    elif choice==5:
        if flag[4]==0:
            import Block_user            
            flag[4]=1
        else:
            importlib.reload(Block_user)
    elif choice==6:
        if flag[5]==0:
            import FEEDBACK_RECORD             
            flag[5]=1
        else:
            importlib.reload(FEEDBACK_RECORD)
    elif choice==7:
        if flag[6]==0:
            import SIGNIN              
            flag[6]=1
        else:
            importlib.reload(SIGNIN)             
    elif choice==8:
        print("Bye...")
        exit()
    else:
        print("Invalid Choice...Try Again!!!")     
    

