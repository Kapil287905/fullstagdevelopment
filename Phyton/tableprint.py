# WAP to show table for any integer number.
# n = int(input("Enter n = "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")


# for i in range(3):
#     print("*")

# for i in range(3):
#     print("*", end=" ")

# for i in range(3):  #wrong patten
#     print(3 * "*")

# star pattan
# r = int(input("Enter row = "))
# c = int(input("Enter coloum = "))
# for i in range(r):
#     for j in range(c):
#         print("*", end=" ")
#     print()

# row value printing
# r = int(input("Enter row = "))
# c = int(input("Enter coloum = "))
# for i in range(r):
#     for j in range(c):
#         print(f"{i}", end=" ")
#     print()

# for i in range(r):
#     for j in range(c):
#         print(f"{j}", end=" ")
#     print()

# r = int(input("Enter row = "))
# c = int(input("Enter coloum = "))
# for i in range(r):
#     for j in range(1,c + 1):
#         print(f"{j}", end=" ")
#     print()

# print row and colum value in matrix format
# r = int(input("Enter row = "))
# c = int(input("Enter coloum = "))
# for i in range(1,r + 1):
#     for j in range(1,c + 1):
#         print(f"[{i},{j}]", end="\t")
#     print()

# 1 to 10 table printing
r = int(input("Enter row = "))
c = int(input("Enter coloum = "))
for i in range(1,r + 1):
    for j in range(1,c + 1):
        print(f"{i*j}", end=" ")
    print()
