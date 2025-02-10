# WAP to validate upir password by entering "admin" as password.
#but gives only 3 attempt fpr wrong password and when it is correct it stop with congrarw msg.

password = "admin"
attempt = 1
while attempt <= 3:
    userpassword = input("Enter password = ")
    if userpassword == password:
        print("password match")
        break
    else:
        print(f"{3-attempt} attempt left")

    attempt += 1