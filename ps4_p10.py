weight=int(input("Enter the weight of a package(in pounds):\n"))
if(weight<=2):
    cost=float(weight*1.50)
    print(f"the Cost of the shipping is ${cost}\n")
elif(weight>2 and weight<=6):
    cost=float(weight*3.00)
    print(f"the Cost of the shipping is ${cost}\n")
elif(weight>6 and weight<=10):
    cost=float(weight*4.00)
    print(f"the Cost of the shipping is ${cost}\n")
elif(weight>10):
    cost=float(weight*4.75)
    print(f"the Cost of the shipping is ${cost}\n")