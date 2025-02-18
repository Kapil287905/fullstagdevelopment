# tuple-collection of element which can different data type but enclose within an parenthesis ()
# it is sequence,order but it immutable

# Empty tuple
# t = tuple()
# print(t,type(t))
# t1 = ()
# print(t1,type(t1))
# t2 = (34)
# print(t2,type(t2))
# t3 = 45, "welcome", 455 # tuple (45, 'welcome', 455)
# print(t3,type(t3))

# tuple1 = (3, "python", True, 6j, None, 56.78, [1, 23],("red", 45),{1: 4})
# print(tuple1, type(tuple1))
# tuple2 = tuple("hello") # tuple ('h', 'e', 'l', 'l', 'o')
# print(tuple2, type(tuple2))

# t4 = tuple(34)
# print(t4,type(t4)) # TypeError: 'int' object is not iterable

# t4 = tuple(34, 45, 56)
# print(t4,type(t4)) # TypeError: tuple expected at most 1 argument, got 3

# t4 = tuple([34, 45, 56])
# print(t4,type(t4))

# t4 = tuple([34, 45, 56],[4,6]) # TypeError: tuple expected at most 1 argument, got 2
# print(t4,type(t4))

# Accessing element via index on tuple
# colors=("red","green","blue","white","grey","black","orange")
# print(colors,len(colors))
# print(colors[0]) # firest->red
# print(colors[-1]) # lasr->orange
# print(colors[len(colors)//2]) # middle->white

# slicing
# print(colors[::-1]) # reversed tuple
# print(colors[3:5])
# print(colors[-3:5])
# print(colors[3:-5]) # ()

# operators
# number = (3, 45, 2, 5)
# x = ("hello", 56, 4.5)
# print(number, id(number))
# print(x)

# print(number+x) # concate tuple
# print(number*5) # repeate for 5 time
# # number += 100
# # print(number) # TypeError: can only concatenate tuple (not "int") to tuple
# number += x
# print(number, id(number)) # 2033796216384

# # print(number > x) # TypeError: '>' not supported between instances of 'int' and 'str'
# a = (1,2)
# b = (4,5,1,2)
# print(a < b)
# print(a == b)
# z = (1,2)
# print(a == z)
# print(a is z)
# print(1 in z)

# # function len(),min(),max(),sorted(),reversed()

# print(b)
# print(len(b))
# print(min(b))
# print(max(b))
# print(sum(b))
# print(sorted(b))
# print("".join(reversed(str(b)))) # )2 ,1 ,5 ,4(

# method .count() and .index()

m = ("hi", 45,56.67, True, 45, "hi")
print(m)
print(m.count(45))
print(m.count("")) # 0
print(m.count(450)) # 0 if not present
# print(m.count(45,"hi")) # TypeError: tuple.count() takes exactly one argument (2 given)

print(m.index(45)) # first index number
# print(m.index("")) # ValueError: tuple.index(x): x not in tuple
# print(m.index(450)) # ValueError: tuple.index(x): x not in tuple