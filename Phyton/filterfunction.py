# filter()-used to check inputs and produce single or many sequence resilt
#Syntax:- filter(function,listofinputs) 

colors = ["red","green","blue","white","black","red"]

# without lambda find red

# def findcolor(choice):
#     return choice == "red"

# print(list(filter(findcolor,colors)))

# with lambda find red

# print(list(filter(lambda x:x == "red",colors)))

# example-1
# show only above 5 number from 1 to 10

print(list(filter(lambda x:x > 5,range(1,11))))