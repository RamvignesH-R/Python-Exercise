while(1):

    month=int(input("Enter the month as number:\n"))
    if(month==1 or month==2 or month==3):
        print("the month is in the first quarter\n")
        break
    elif(month==4 or month==5 or month==6):
        print("the month is in the second quarter\n")
        break
    elif(month==7 or month==8 or month==9):
        print("the month is in the third quarter\n")
        break
    elif(month==10 or month==11 or month==12):
        print("the month is in the fourth quarter")
        break
    else:
        print("ERROR!!number is not between 1 and 12")
    


