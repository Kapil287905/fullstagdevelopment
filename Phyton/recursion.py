# function calling itself
# def display():
#     print("welcome")
#     display()

# display()

# to stop recursion
# def display():
#     print("welcome")
#     password = input("Enter password = ")
#     if password == "admin":
#         return
#     else:
#         display()

# display()

# Recursion used stak data structure
# find factorial for any interger number

# n = int(input("Enter n = "))

# def factorial(n):
#     if n > 1:
#         return n * factorial(n-1)
#     else:
#         return 1
    
# print(factorial(n))

# WAP to sum of digit by using reccursion
n = int(input("Enter n = "))

def sumofdigit(n):
    if n > 0:
        return n % 10 +sumofdigit(n//10)
    else:
        return 0
    
print("sum of digit",sumofdigit(n))

