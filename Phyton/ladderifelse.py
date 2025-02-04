# WAP to monthnumber from user and show Month and number of days
# try:
#     month = int(input("Enter monthnumber= "))
#     if month == 1:
#         print(f"{month} is January and has 31 days")
#     elif month == 2:
#         year=int(input("Enter year="))
#         if year%4==0:
#             print(f"{year} is leap and {month} is Fabuary and has 29 days")
#         else:
#             print(f"{year} is leap and {month} is Fabuary and has 28 days")
#     elif month == 3:
#         print(f"{month} is March and has 31 days")
#     elif month == 4:
#         print(f"{month} is April and has 30 days")
#     elif month == 5:
#         print(f"{month} is MAy and has 31 days")
#     elif month == 6:
#         print(f"{month} is June and has 30 days")
#     elif month == 7:
#         print(f"{month} is July and has 31 days")
#     elif month == 8:
#         print(f"{month} is August and has 31 days")
#     elif month == 9:
#         print(f"{month} is September and has 30 days")
#     elif month == 10:
#         print(f"{month} is Octomber and has 31 days")
#     elif month == 11:
#         print(f"{month} is November and has 30 days")
#     elif month == 12:
#         print(f"{month} is December and has 31 days")
#     else:
#         print("Please enter month number between 1 to 12")
# except:
#     print("invlid input")



# WAP 
print("Currency conversion fore below country")
print("Country Name and code\nIndia-INR\nUSA-USD\nEurope-EUR")
try:
    fromcountry = input("Enter fromcurrency country code= ")
    tocountry = input("Enter tocurrency country code= ")
    amount = float(input("Enter amount= "))
    if fromcountry.upper() == "INR" and tocountry.upper() == "INR":
        rates=1
    elif fromcountry.upper() == "INR" and tocountry.upper() == "USD":
        rates=0.011
    elif fromcountry.upper() == "INR" and tocountry.upper() == "EUR":
        rates=0.011
    elif fromcountry.upper() == "USD" and tocountry.upper() == "USD":
        rates=1
    elif fromcountry.upper() == "USD" and tocountry.upper() == "INR":
        rates=86.96
    elif fromcountry.upper() == "USD" and tocountry.upper() == "EUR":
        rates=0.97
    elif fromcountry.upper() == "EUR" and tocountry.upper() == "EUR":
        rates=1 
    elif fromcountry.upper() == "EUR" and tocountry.upper() == "INR":
        rates=89.74
    elif fromcountry.upper() == "EUR" and tocountry.upper() == "USD":
        rates=1.03
    else:
        print("invalid country code")

    totalprice = rates * amount
    print(F"{amount} {fromcountry} is {totalprice} {tocountry}")
except:
    print("invlid input")