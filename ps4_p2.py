length=float(input("Enter the length (in cm):\n"))
if(length<=0):
    print("the input is invalid\n")
else:
    inches=(length/2.54)
    print("the converted inches is ",inches)