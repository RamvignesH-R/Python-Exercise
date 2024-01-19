x=int(input("Enter the number to get Syracuse sequence:\n"))
print(f"the Syracuse sequence of the number {x} is \n{x}")
while(x!=1):
    if(x%2==0):
        syr=int(x/2)
        x=syr
        print(x)
    else:
        syr=int(3*x+1)
        x=syr
        print(x)