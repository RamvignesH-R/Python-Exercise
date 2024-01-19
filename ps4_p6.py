while(1):
    choice=input("Enter any characters among (A,B,C)\n")
    match choice:
        case 'A' | 'a':
            print("Apple\n")
            break
        case 'B' |'b':
            print("Banana\n")
            break
        case 'C'|'c':
            print("Coconut\n")
            break
        case _:
            print("Invalid input.Enter A,B,C\n")