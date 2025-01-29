# Datatypes
# Built-in (number-intmfloat,complex),string,none,boolean
# Collection/Reference/sequence-(list,tuple,set,dict)
# u-defined-class

n = 23654
print(type(n), n) # int
n = -125487
print(type(n), n) # int
n = "23654"
print(type(n), n) # str
n = 236.54
print(type(n), n) # float
s = "welcome"
print(type(s), s) # str
char = "A"
print(type(char), char) # str
x = 131321321321321321321321321321321321321321321321321
print(type(x), x) # int
x = 131321_321321_32132132_1321321_32132_13213_213213_21321321
print(type(x), x) # int
m = 5J
# m = 5k #error
print(type(m),m) # complex j or J as real number
m = 1 + 89j
print(type(m),m) # complex j or J as real number

flag1 = True
flag2 = False
flag3 = "True"
print(type(flag1),flag1) # bool
print(type(flag2),flag2) # bool
print(type(flag3),flag3) # str
q = None
print(type(q),q) # Nonetype

n = ""
print(type(n), n) # str

#k = none #error

# Collection data type-set of element/values enclosed within bracket
tuple1 = (423,True,5j,"welcomr",None,4.45)
print(type(tuple1),tuple1) # tuple
tuple2 = (423)
print(type(tuple2),tuple2) # int
tuple3 = 423,True,5j,"welcomr",None,4.45
print(type(tuple3),tuple3) # tuple

list1 = [423,True,5j,"welcomr",None,4.45]
print(type(list1),list1) # list
list2 = [423]
print(type(list2),list2) # list

set1 = {423,True,5j,"welcomr",None,4.45}
print(type(set1),set1) # set
set2 = {423}
print(type(set2),set2) # set

dict1 = {"name":"pooja","grade":"A"}
print(type(dict1),dict1) # dict
dict2 = {1:1,2:4,3:9,4:16,5:25}
print(type(dict2),dict2) # dict


