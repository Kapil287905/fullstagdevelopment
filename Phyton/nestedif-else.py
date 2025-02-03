#WAp to check entred interger number is zero,+ve and -ve number
# try:
#     n = int(input("enter n="))
#     if n == 0:
#         print(f"{n} is zero")
#     else:
#         if n > 0:
#             print(f"{n} is +ve number")
#         else:
#             print(f"{n} is -ve number") 
# except:
#     print("invlid input")

# WAP to show Square abd cube of any interger number flow below case
# note
# Test case-1) Id empty input then shoe invalid input
# Test case-2) if number is zero or less than zero also ir will show number cant be zero
# try:
#     n = int(input("enter n="))
#     if n != 0:
#         sq = n**2
#         cube = n**3
#         print(f"Square={sq} and cube={cube}")
#     else:
#        print("Entered number can't be zero")             
# except:
#     print("invlid input")


# WAP to find smallest number among any positive three interger number
# try:
#     a = int(input("enter a="))
#     b = int(input("enter b="))
#     c = int(input("enter c="))
#     if a>0 and b>0 and c>0:
#         if a<b and a<c:
#             print(f"{a} is smallest number")
#         else:
#             if b<c:
#                  print(f"{b} is smallest number")
#             else:
#                  print(f"{c} is smallest number")
#     else:
#         print("Entered number can't be zero or -ve number")
# except:
#     print("invlid input")

# try:
#     a = int(input("enter a="))
#     b = int(input("enter b="))
#     c = int(input("enter c="))
#     if a<b and a<c:
#         print(f"{a} is smallest number")
#     else:
#         if b<c:
#                 print(f"{b} is smallest number")
#         else:
#                 print(f"{c} is smallest number")
# except:
#     print("invlid input")

# try:
#     a = int(input("enter a="))
#     b = int(input("enter b="))
#     c = int(input("enter c="))
#     if a<b and a<c:
#         print(f"{a} is smallest number")
#     elif b<c:
#             print(f"{b} is smallest number")
#     else:
#             print(f"{c} is smallest number")
# except:
#     print("invlid input")

# WAP to show wellcome msg fore userr according to entred username

user = input("enter username=")
if user == "admin":
    print("Welcome Admin! ypu had all permition")
elif user == "testuser":
    print("Welcome testuser! you all read and write permission")
elif user == "guest":
     print("Welcome guest! you have only read permission")
elif user == "":
    print("please enter correct username")
else:
    print("invalid username")



















