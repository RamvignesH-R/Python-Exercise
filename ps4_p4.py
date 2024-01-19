month=int (input("Enter the month in the number:\n"))
day=int (input("Enter the day in the number:\n"))
year=int (input("Enter the year in the numbers(only last 2 digits:eg.2022==>22):\n"))
if(month*day==year):
    print("the date is magic")
else:
    print("the date is not magic")