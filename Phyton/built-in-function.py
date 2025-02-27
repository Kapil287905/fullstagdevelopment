"""
Function-block of code use to avoid repeatation and called n number of times
Type of function
1)Built-in finction (system defined)
len(),min(),max(),char(),ord(),print(),input(),range(),reversed(),sorted(),frozenset()
2) User-defined (body of function,calling of function)
"""

# Built-in-function
# bin(),hex(),oct(),hrlp(),pow(),round(),divmod(),zip(),slice(),enumerate()


# a = 3
# print(a)
# print(bin(a)) # binary
# print(oct(a)) # octal
# print(hex(a)) # hexadecimal

# # help()
# # print(help("def"))
# print(help("jkj"))

# pow(),round(),divmod()
# print(pow(2,3))
# print(2**3)
# print(round(34.454546))
# print(round(34.554546))
# print(round(34.554546,4))
# print(round(34.554566,4))
# print(divmod(5,3)) # 5//3(1),5%3(2) # gives ans in tupple(1,2)
# print(5//3,5%3)

# zip() -> packing data into one element
# names = ["rohan","komal","pooja"]
# grade = ["A","O","A+"]
# percentage = [89.45,67.78]
# # print(list(zip(names,grade)))
# # # print(list(zip(names,grade,percentage))) # can't show pooja A+
# # for i in names,grade:
# #     # print(i)
# #     print(i[0],end=" ")

# print(tuple(zip(names,grade,percentage)))
# print(set(zip(names,grade,percentage)))
# print(dict(zip(names,grade)))
# # print(dict(zip(names,grade,percentage))) # not possible only 2 ValueError: dictionary update sequence element #0 has length 3; 2 is required

# unzip(zip("variable"))-unpacking data into sequence element
# students = [("rohan","A"),("komal","o"),("pooja","A+")]
# # students = [("rohan","A"),("komal","o"),("pooja")] # for 3 element [('rohan', 'komal', 'p'), ('A', 'o', 'o')]
# # students = [("rohan","A"),("komal","o"),("pooja",None)]
# # print(students)
# print(list(zip(*students)))
# print(set(zip(*students)))
# print(tuple(zip(*students)))
# # print(dict(zip(*students))) # error

# students = [["rohan","A"],["komal","o"]]
# print(dict(zip(*students)))

# students = [("rohan","A"),("komal","o")]
# print(dict(zip(*students)))

# slice()
# colors = ["red","green","blue","white","grey","orange"]
# ans = slice(2,5)
# print(colors[ans])
# print(colors[2:5])

# msg = "welcome to puthon"
# print(msg[ans])

# enumerate()-> generate dataset by adding index number
# colors = ["red","green","blue","white","grey","orange"]
# print(colors)
# # print(list(enumerate(colors))) # start index from 0
# # print(list(enumerate(colors,3))) # start index from 3
# # print(tuple(enumerate(colors)))
# print(dict(enumerate(colors)))
# print(dict.fromkeys(colors,0))
# # print(set(enumerate(colors)))

# iter()-> genetator function,it perfoms withoutloop we can itrate sequence object 
colors = ["red","green","blue"]
print(colors)
newdata = iter(colors)
print(newdata, type(newdata)) # won't show you result
first = next(newdata)
print(first)
seccond = next(newdata)
print(seccond)
third = next(newdata)
print(third)
# forth = next(newdata) # StopIteration error
# print(forth)