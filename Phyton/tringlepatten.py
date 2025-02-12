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

r = int(input("Enter row = "))
for i in range(r):
    for j in range(r-i - 1):
        print(" ", end=" ")
    for k in range(i+1):
         print("*", end=" ")
    print()