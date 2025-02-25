# dictionary:-collection of different data type but written as key:value pair enclosed 
# within {}.No index but keyindexing,unorder nut follow key order and no slicing and no
# repeated keys but calue can be repeated

# empty dict
# d = {}
# print(d,type(d))
# d = ()
# print(d,type(d))
# d = {1:1}
# print(d,type(d))
# d = {1:1,1:6}
# print(d,type(d))
# d = {"name":"komal", "rollnum": 34,"grade":"A"}
# print(d,type(d))
# d = {"name":"Roshan"}
# print(d,type(d))

# withot methods add update abd remove
# books = {}
# print(books)
# books["title"] = "python"
# print(books)
# books["title"] = "java"
# print(books)
# books["author"] = "jj"
# print(books)
# books["price"] = 800
# print(books)
# books["publisher","qty"] = "techmax",7 # tuple
# print(books)
# books=dict(isbn=1111,dop="12-09-2009") # newly assign
# print(books)

# print("--------------------")
# # delete/remove via keyname
# del books["isbn"]
# print(books)

# # del books["title"] # KeyError: 'title' not present
# # print(books)

# update
colors = {1:"red",2:"blue",3:"green",4:"white"}
print(colors)
colors[2] = "pink"
print(colors)
colors[9] = "orange" #key not present then it adds
print(colors)
colors[8] = "red" #key not present then it adds
print(colors)

# reading element
print(colors[1]) # red


