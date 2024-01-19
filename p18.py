a=float(input("Enter the number to find the square root:\n "))
x=a
while(1):
    y=(x+(a/x))/2
    if abs(y-x)<0.0001:
        break
    x=y
print(f"The square root of {a} is approximately {y}.")