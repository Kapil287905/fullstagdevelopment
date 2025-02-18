# list=collection of different data type element enclose
# sequence,order,mutable data type

# empty list

list1 = []
print(list1, type(list1))

list2 = list()
print(list2, type(list2))

list3 = [45]
print(list3, type(list3))

list4 = [45,"js", True, 5j, 3.4, ("red","green"),[35,35], {2,5},{1:35}]
print(list4, type(list4))

list5 = list("welcome")
print(list5, type(list5))
 
# list6 = list(456456) # error
# print(list6, type(list6))

# indexing
mylist = ["red","green","blue"]
print(mylist[0]) # firest->red
print(mylist[-1]) # lasr->orange
print(mylist[len(mylist)//2]) # middle->white

# slicing
print(mylist[0:1]) # red
print(mylist[-1:1]) # []
print(mylist[-1:]) # ['blue']