hour=int(input("Enter an hour between 1 and 12:\n"))
unit=int(input("Enter whether it a.m(1) or p.m(2):\n"))
future=int(input("How many hours ahead?\n"))
futureHour=(hour+future)%12
if(futureHour==0):
    futureHour=12
if(hour+future)//12%2==1:
    if(unit==1):
        print(f"The New hour:{futureHour} pm\n")
    elif(unit==2):
        print(f"The New hour:{futureHour} am\n")
    else:
        print("ERROR IN AM/PM\n")