# WAP to print all odd number from 1 to 100 using for loop

# for i in range(1,101,2):
#     print(i)


# for i in range(1,101,2):
#     if i %2 != 0:
#         print(i)

# # WAP to 10 to 1 number
# for i in range(10,0,-1):
#      print(i)

# WAP ro 1 to 10 number and show sum of them
# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     print(i)
# print("sum of 1 to 10 = ",sum)

# WAP to show factorial of any number
n = int(input("Enter n = "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} = {fact}")