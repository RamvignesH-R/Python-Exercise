year=int (input("enter the year in the numbers:\n"))
if(year%4==0 ):
    print("It is a Leap year\n")
elif(year%100==0 and year%400==0):
    print("It is a Leap year\n")
else:
    print("It is not a leap year\n")