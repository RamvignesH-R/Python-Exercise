credit=int (input("Enter the number of college credits in numbers\n"))
if(credit>90):
    print("Status:SENIOR\n")
elif(credit>60):
    print("Status:JUNIOR")
elif(credit>30):
    print("Status:SOPHOMORE")
else:
    print("Status:FRESHMAN")