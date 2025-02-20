# list methods

# Adding ekement append(),insert()

# colors = []
# print(colors)
# colors.append("red")
# print(colors)
# colors.append("green")
# print(colors)
# # colors.append("blue","white") # TypeError: list.append() takes exactly one argument (2 given)
# colors.append(["blue","white"])
# print(colors)
# colors.append(("blue","white"))
# print(colors)
# colors.append({"blue","white"})
# print(colors)
# x = ["blue","white"]
# colors.append(x)
# print(colors)

# # for i in colors:
# #     print(i)

# colors.append("black",0) # index not allowed

# WAP to create mylist add number as per count entred by user
mylist = []
counter = int(input("Enter list counter = "))

for i in range(counter):
    n = int(input(f"Enter {i+1} = "))
    mylist.append(n)

print(mylist)

# 1) length od mylist
# count = 0
# for i in mylist:
#     count += 1
# print(f"length of mylist ={count}")

# 2) sorting asscending or descending
# # Ascending order
# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] < mylist[j]:
#             mylist[i],mylist[j] = mylist[j],mylist[i]
# print("Ascending order=",mylist)

# # descending order
# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] > mylist[j]:
#             mylist[i],mylist[j] = mylist[j],mylist[i]
# print("Descending order=",mylist)

# 3) find 2nd highest ekement
# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] > mylist[j]:
#             mylist[i],mylist[j] = mylist[j],mylist[i]
# print("Descending order=",mylist)
# print("2nd highest",mylist[1])

# show newmylist witout duplication any element
# newmylist = []
# for i in mylist:
#     if i not in newmylist:
#         newmylist.append(i)
# print(newmylist)           

# count of element

# find replace element
# sum of all element
# sum = 0
# for i in mylist:
#     print(sum(mylist))

# show even and odd number in seperate list
