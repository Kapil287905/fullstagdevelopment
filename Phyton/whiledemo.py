'''
while syntax

initialization
while condition
    stmt
    stmt
    increment/decrement

'''

# while True:
#     print("welcome")
#     break #to terminate loop

# while False:
#     print("hello")

# while 4+5: # true thats why it takes to infinite loop
#     print("show")
#     break #to terminate loop

# WAP to print 1 to 5 number
# start = 1
# end = 5
# while start <= end:
#     print(f"{start}", end=" ")
#     start+=1

# i = 1
# while i <= 5:
#     print(i, end=" ")
#     i += 1

# WAP to print any number in series and in increment by 1
#as per entred start and end numbew

# try:
#     start = int(input("Enter start number= "))
#     end = int(input("Enter end number= "))
#     if start < end:
#         while start <= end:
#             print(f"{start}")
#             start+=1
#     else:
#         print("start number must be less than end number")
# except:
#     print("invalid input")

# Infinite case (when we work with ascending order(increment))
# case-1 (if we forget to put increment)
# i = 1
# while i <= 5:
#     print(i)

# case-2 (if we putted decrement instead of increment)
# i = 1
# while i <= 5:
#     print(i)
#     i = i - 1

# WAP to print 10 to 1.
# i=10
# while i >= 1:
#     print(i,end=" ")
#     i-=1

# Infinite case (when we work with descending order(decrement))
# case-1 (if we forget to put decrement)
# i = 10
# while i >= 1:
#     print(i)

# case-2 (if we putted increment instead of decrement)
# i = 10
# while i >= 1:
#     print(i)
#     i = i + 1

# case-3 wrong initialiaztion (start)
i = 10
while i >= 10:
    print(i)
    i += 1