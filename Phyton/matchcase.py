# WAP to check 0 to 6 as day number and print respective dayname

try:
    daynumber=int(input("Enter day number (0-6): "))
    match daynumber:
        case 0:
            print(f"{daynumber} is Sunday")
        case 1:
            print(f"{daynumber} is Monday")
        case 2:
            print(f"{daynumber} is Tuestay")
        case 3:
            print(f"{daynumber} is Wednesday")
        case 4:
            print(f"{daynumber} is Thurday")
        case 5:
            print(f"{daynumber} is Friday")
        case 6:
            print(f"{daynumber} is Saturday")
        case _:
            print("Incorrect Day number")        
except:
    print("Invalid input")