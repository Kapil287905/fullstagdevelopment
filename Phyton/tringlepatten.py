# left incremental tringle
# r = int(input("Enter row = "))
# for i in range(r):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# for i in range(r):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# for i in range(1,r + 1):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# c = int(input("Enter coloum = "))
# for i in range(r):
#     for j in range(c):
#         if i == j:
#              print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()

# left decremental tringle
# r = int(input("Enter row = "))
# for i in range(r,0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# right incremental tringle
# r = int(input("Enter row = "))
# for i in range(1,r +1):
#     for j in range(r):
#         print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# for i in range(r):
#     for j in range(r-i - 1):
#         print(" ", end=" ")
#     for k in range(i+1):
#          print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# c = int(input("Enter column = "))
# count = 1
# for i in range(r):
#     for j in range(c):
#         print(f"{count}", end=" ")
#         count = count + 1
#     print()


# r = int(input("Enter row = "))
# c = int(input("Enter column = "))
# for i in range(1,r + 1):
#     count = i
#     for j in range(c):
#         print(f"{count}", end=" ")
#         count = count + 5
#     print()

# r = int(input("Enter row = "))
# for i in range(r):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(r-i):
#          print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# for i in range(1,r +1):
#     for j in range(r-i):
#         print(" ", end="")
#     for k in range(i):
#          print("*", end=" ")
#     print()


# r = int(input("Enter row = "))
# for i in range(r):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(r - i):
#          print("*", end=" ")
#     print()

# r = int(input("Enter row = "))
# count = 1
# for i in range(1,r +1):
#     for j in range(r-i):
#         print(" ", end="")
#     for k in range(i):
#          print(f"{count}", end=" ")
#          count = count + 1
#     print()

# r = int(input("Enter row = "))
# count = 1
# for i in range(r):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(r - i):
#           print(f"{count}", end=" ")
#           count = count + 1
#     print()

# r = int(input("Enter row = "))
# for i in range(1,r):
#     for j in range(r-i):
#         print(" ", end="")
#     for k in range(i):
#          print("*", end=" ")
#     print()
# for i in range(r):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(r-i):
#          print("*", end=" ")
#     print()

# write a code tp print the following patten 
r = int(input("Enter row = "))
c = int(input("Enter column = "))
count = 1
for i in range(r):
    for j in range(c):
        if i % 2 == 0:
            if j % 2 != 0:
                print("*", end=" ")
            else:
                print(f"{count}", end=" ")
                count = count + 1
        else:
            if j % 2 != 0:
               print(f"{count}", end=" ")
               count = count + 1 
            else:
                print("*", end=" ")
    print()