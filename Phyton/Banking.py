while True:
    try:
        print("welcome to Mybank\n----------------------------------")
        print("1:Create Account\n2:Credit Account\n3:Debit Account\n4:Show Balance\n5:Exit")
        choice=int(input("Enter choice number= "))
        if choice == 1:
            name=input("Enter your name= ")
            amount=float(input("Enter amount to open account= "))
            if amount>=1000:
                print(f"{name}, Congrates your account created successfully and account number is 5555")
                accountnum=5555
            else:
                print("Amount must be greater than or equal to 1000")
        elif choice == 2:
            newaccountmum=int(input("Enter yopuA/c number to verify= "))
            if newaccountmum == accountnum:
                creditamt=float(input("Enter credit to verify= "))
                if creditamt > 0:
                    amount+=creditamt
                    print("Amount credited successfully")
                else:
                    print("credit amount must be greater zero")
            else:
                print("Invalid account number. Try again")
        elif choice == 3:
            newaccountmum=int(input("Enter yopuA/c number to verify= "))
            if newaccountmum == accountnum:
                debitamt=float(input("Enter credit to verify= "))
                if debitamt > 0 and debitamt <= amount:
                    amount-=debitamt
                    print("Amount debited successfully")
                else:
                    print("Debit amount must be greater zero or insufficient balance")
            else:
                print("Invalid account number. Try again")
        elif choice == 4:
            newaccountmum=int(input("Enter yopuA/c number to verify= "))
            if newaccountmum == accountnum:
                print("Your current balance= ",amount)
            else:
                print("Invalid account number. Try again")
        elif choice == 5:
            print("Thanl you for using our service!!!")
            break
        else:
            print("Invalid choice number")
    except:
        print("Invalid input")