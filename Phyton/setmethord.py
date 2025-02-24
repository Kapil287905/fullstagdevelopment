# set method

# adding element

# mylist = set()
# print(mylist)
# mylist.add("red")
# print(mylist)
# mylist.add("red") # no error but can't add because already present
# print(mylist)
# mylist.add(("green","blue"))
# print(mylist)
# x = ("black",45,"white")
# mylist.add(x)
# print(mylist)

# WAP to take number from user and show sum of them as per count entred by user

# count = int(input("enter count number = "))
# sum = 0
# myset = set()
# for i in range(count):
#     n = int(input(f"enter {i+1} number = "))
#     myset.add(n)
#     sum = sum + n
# print(myset)
# print(f"sum of above number = ",sum)

# copy()
# x = {1,2,3}
# y = {3,4,5,6}
# print(x)
# print(y)
# x = y.copy()
# print(x)

# #update()
# z = {"red","blue"}
# z.update(x) # add element
# print(z) # {3, 'blue', 4, 5, 6, 'red'}
# z.update((45,56))
# print(z)

# z.update({8,100,200})
# print(z)

# z.update([99,88])
# print(z)

# # remove element
# z.remove(88)
# print(z)

# z.remove(188) # KeyError: 188 if element not present
# print(z)

# z.discard(188) # it won't show error if element not present
# print(z)
# z.discard(100)
# print(z)

# z.pop() # as per interpreter it remove first element
# print(z)
# z.pop()
# print(z)

# z.clear()
# print(z)

# del z
# print(z)


# WAP to take student data as name,marks,grade into set for 3 student
# students = set()
# for i in range(3):
#     name = input(f"enter {i+1} student name = ")
#     marks = int(input(f"enter {i+1} student marks = "))
#     grade = input(f"enter {i+1} grade name = ")
#     # students.update((name,marks,grade))
#     students.add((name,marks,grade))
# print(students)

# a = {1,2,3,4}
# b = {1,2,3}
# c = {11,12} 
# print(a.issuperset(b)) # True
# print(a>b) # True
# print(b.issubset(a)) # True
# print(a>b) # True
# print(a.isdisjoint(b)) # False if intersection is not empty then it is False  
# print(a.isdisjoint(c)) # True if intersection is empty then it is True

# frozenset() are immutable
s = {"red","green"}
print(s)
s.add("black")
print(s,type(s))
s = frozenset(s)
print(s,type(s))
# s.add("white") # AttributeError: 'frozenset' object has no attribute 'add'
print(s)