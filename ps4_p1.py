temp=float(input("Enter the temperature:\n"))
unit=input("Enter the unit of the temperature(C-Celsius and F-Fahrenheit):\n")
if (unit=='c'or unit=='C'):
    f=((9/5)*temp)+32
    print("the converted temperature is (in Fahrenheit) ",f)
elif(unit=='f'or unit=='F'):
    c=(5/9*(temp-32))
    print("the converted temperature is (in celsius) ",c)