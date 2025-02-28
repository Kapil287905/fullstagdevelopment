# 2) type of argument
# 1) positional Argument
# 2) Keyword Argument

# positional Argument
name = "raj"
rollnum = 101

# case-1
# def showdata(x,y=1):
#     print(f"My name is {x} and rollnumber is {y}")

# showdata(name,rollnum) # raj 101
# showdata(name) # raj 1
# showdata(rollnum) # 101 1

# case-2
# def showdata(x="komal",y): # syntax Non-default argument follows default argument
#     print(f"My name is {x} and rollnumber is {y}")
# showdata(rollnum)

# case-3
# def showdata(x="komal",y=2):
#     print(f"My name is {x} and rollnumber is {y}")

# # showdata(x,y) # error x and y are local
# showdata(name,rollnum)
# showdata(rollnum)

# case-4
# def showdata(name="komal",rollnum=2):
#     print(f"My name is {name} and rollnumber is {rollnum}")

# showdata(name,rollnum)  # raj 101

# def showdata(name="komal",rollnum=2):
#     name = "a"
#     rollnum = 11
#     print(f"My name is {name} and rollnumber is {rollnum}")

# showdata(name,rollnum)  # a 11

# keywords Argument
#case-1
# def showdata(name,rollnum):
#     print(f"My name is {name} and rollnumber is {rollnum}")

# showdata(name,rollnum) # raj 101
# # showdata(name="komal",rollnum) # syntax error
# showdata(name="komal",rollnum=102) # komal 102
# showdata(name,rollnum=102) # raj 102
# # showdata(x="komal",y=102) # TypeError: showdata() got an unexpected keyword argument 'x'

#case-2
def showdata(name,rollnum=1111):
    print(f"My name is {name} and rollnumber is {rollnum}")

showdata(name="komal")