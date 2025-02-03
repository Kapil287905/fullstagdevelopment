# if True:
#     print("wellcome True")

# if False:
#     print("wellcomr False") #won't show because

# if 10:
#     print("wellcome 10")

# if 10 - 5:
#     print("wellcome 10 - 5")

# if 0:
#     print("wellcome 0")

# #empty block
# if True:
#     pass

# if 5 == 5:
#     pass

# # wAP check numbe is zero or not
# #rarnary
# n = int(input("enter n="))
# ans= f"{n} is zero" if n == 0 else f"{n} is not zero"
# print(ans)

# n = int(input("enter n="))
# if n == 0:
#     print(f"{n} is zero")

# print(f"{n} is not zero")

# insterd of only if use if-else block
# n = int(input("enter n="))
# if n == 0:
#     print(f"{n} is zero")
# else:
#     print(f"{n} is not zero")

# flag = True
# if flag:
#     print("it is working")

# if "": #False
#     print("Empty string working") #won't show

# if None: #False
#     print("None string working") #won't show

#WAp to check enter number is +ve or -ve
# n = int(input("enter n="))
# if n > 0:
#     print(f"{n} is +ve")
# else:
#     print(f"{n} is -ve")

#WAp to check enter number is even or odd
# n = int(input("enter n="))
# if n % 2==0:
#     print(f"{n} is even number")
# else:
#     print(f"{n} is odd number")

#WAP to show greater number amoung any two number
# a = int(input("enter a="))
# b = int(input("enter b="))
# if a > b:
#     print(f"{a} is greater number")
# else:
#     print(f"{b} is greater number")

#WAP to check entered year is leap year or not
# year = int(input("enter year="))
# if year % 4 == 0:
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

#WAP to show profit and loss as per entered costprice and selling price
# cp = int(input("enter cost price="))
# sp = int(input("enter selling pprive="))
# if sp > cp:
#     profit = sp - cp
#     print(f"Congrate! you earned ptofit of {profit}Rx/-")
# else:
#     loss = cp - sp
#     print(f"sorry! you had loss of {loss}Rx/-")


cp = int(input("enter cost price="))
sp = int(input("enter selling pprive="))
if sp == cp:
    print("No profit no loss")
else:
    if sp > cp:
        profit = sp - cp
        print(f"Congrate! you earned ptofit of {profit}Rx/-")
    else:
        loss = cp - sp
        print(f"sorry! you had loss of {loss}Rx/-")