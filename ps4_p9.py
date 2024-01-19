people=int (input("Enter the number of people attending cookout:\n"))
hotdogPerPeop=int (input("Enter thre number of the hot dogs each person will be given:\n"))
requiredHotdogs=people*hotdogPerPeop
packageHotdog=(requiredHotdogs+9)//10 
leftoverHotdog=packageHotdog*10-requiredHotdogs
requiredBun=people*hotdogPerPeop
packageBun=(requiredBun+7)//8
leftoverBun=packageBun*10-requiredBun
print("\nHot Dog Cookout Calculator Results:")
print(f"Minimum number of hot dog packages required: {packageHotdog}")
print(f"Minimum number of hot dog bun packages required: {packageBun}")
print(f"Number of hot dogs left over: {leftoverHotdog}")
print(f"Number of hot dog buns left over: {leftoverBun}")