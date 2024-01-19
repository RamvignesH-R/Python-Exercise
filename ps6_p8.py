str=input("Enter the sentence:\n")
print("the third word of the sentence")
arr=str.split()
print(arr[2])
print("every third word of the sentence")
i=2
while(i<len(arr)):
    print(arr[i])
    i+=3