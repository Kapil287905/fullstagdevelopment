# WAP to check enter number  is prime or not
# n = int(input("Enter n = "))
# flag = False
# if n==1:
#     print(f"{n} is not a prime number")
# else :
#     for i in range(2,n):
#         if n%i == 0:
#             flag = True
#             break
    
#     if flag == True:
#         print(f"{n} is not a prime number")
#     else:
#         print(f"{n} is a prime number")

# WAP to check enter number is perfect or not
n = int(input("Enter n = "))
sum=1
for i in range(2,n):
    if n%i == 0:
        sum = sum + i
if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
