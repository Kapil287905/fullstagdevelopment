# set - collection of dofferent datatype enclosed within {}
# non-sequence,no-index no slicing but mutable, contains duplicate element but 
# while  reading/showing it avoid duplication

# Empty set

# s = {} 
# print(s, type(s)) # dict
# s = set()
# print(s, type(s)) # set
# s1 = {34}
# print(s1, type(s1)) # set
# s2 = {"Hello",True,56j,None,67.78}
# print(s2, type(s2)) # set
# s3 = {"red",45,45,None,78,45}
# print(s3, type(s3)) # set
# s4 = {(1,2),[1,2],{1,2},56,45}
# print(s4, type(s4)) # TypeError: unhashable type: 'list'
# s5 = {(1,2),(1,2),{1,2},56,45}
# print(s5, type(s5)) # TTypeError: unhashable type: 'set'
# s6 = {(1,2),(1,2),(1,2),56,45}
# print(s6, type(s6)) # set

# no index on slising
# color = {"red","green","blue","white"}
# # print(color[0]) # TypeError: 'set' object is not subscriptable
# # print(color[1:]) # TypeError: 'set' object is not subscriptable

# newcolors = list(color)
# print(newcolors)
# newcolors.append("black")
# color = set(newcolors)
# print(color)

# operators

# a = {1,2,3}
# b = {3,4,"java"}
# c = {5,6,7,9}
# d = {1,2,3,8,9,10}
# print(a)
# print(b)
# print(c)
# print(d)
# # print(a+b) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# # print(a+c) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# # print(a*b) # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# # print(a*5) # unsupported operand type(s) for *: 'set' and 'int'
# print(a-b) # {1, 2} difference of a to b (unmatched of a)
# print(b-a) # {'java', 4}  difference of a to b (unmatched of b)
# print(a-d) # set()
# print(a==b) # False
# print(a is b) # False
# print(a in d) # False
# print(2 in d) # True
# print(a>b) # False a is not superset of d
# print(d > a) # True d is superset of a

# set operations methods are union(),intersection(),difference(), symmetric_difference()
x = {1,2,3,4}
y = {2,4,5,6}
print("x = ",x)
print("y = ",y)

print("union of x to y", x.union(y))
print("union of y to x", y.union(x))
print("union of x to y", x|y)

print("intersection of x to y", x.intersection(y))
print("intersection of y to x", y.intersection(x))
print("intersection of x to y", x&y)

print("difference of x to y", x.difference(y)) # unmatched of x
print("difference of y to x", y.difference(x)) # unmatched of y
print("difference of x to y", x-y) # unmatched of x

print("symmetric_difference of x to y", x.symmetric_difference(y)) # unmatched of x and y
print("symmetric_difference of y to x", y.symmetric_difference(x)) # unmatched of x and y
print("symmetric_difference of x to y", x^y) # unmatched of x and y
