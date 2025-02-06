# try:
#     i = 1
#     sum = 0
#     while i <= 10: 
#         print(i)
#         sum+=i
#         i += 1
#         print("Sum", sum)
#     print("sum of 1 to 10 = ",sum)
# except:
#     print("invalid input")

# WAP to show sum of entred number as per count

try:
    count = int(input("Enter count for number = "))
    i = 1
    sum = 0
    while i <= count:
        n = int(input(f"Enter {i} nimber = "))
        sum+=n
        i+=1 
    print("sum of above = ",sum)   
except:
    print("invalid input")