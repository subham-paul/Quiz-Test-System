import importlib
flag=[0,0,0,0]
while True:
    print("\t----------------------")
    print("\t*** User Profile ***")
    print("\t----------------------")
    print("1:Play Quiz.")
    print("2:Feedback.")
    print("3:Show all results")
    print("4:Back.")
    print("5:Exit.")
    choice=int(input("Enter your choice:"))
    if choice==1:
        if flag[0]==0:
            import Play_quiz     
            flag[0]=1
        else:
            importlib.reload(Play_quiz)
    elif choice==2:
        if flag[1]==0:
            import Feedback            
            flag[1]=1
        else:
            importlib.reload(Feedback)
    if choice==3:
        if flag[2]==0:
            import show_all_result     
            flag[2]=1
        else:
            importlib.reload(show_all_result)            
    elif choice==4:
        if flag[3]==0:
            import SIGNIN                 
            flag[3]=1
        else:
            importlib.reload(SIGNIN)
    elif choice==5:
        print("OKK..")
        exit()
    else:
        print("Invalid Choice...Try Again!!!")
