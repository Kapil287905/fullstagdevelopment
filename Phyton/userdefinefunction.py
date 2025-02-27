'''
# user defined function
Syntax:-
1) Definition of function(function body)
def function_name(prm1,prm2.prm3......(optional))
    stmt
    block
    return expression/stmt/variable(optional)
2) calling if function
function_name(arg1,arg2,arg3,......(optional))

Note:-
1) Whenever the function is written it is compulsory to call a function otherwise ir won't start enecution
2) calling of function must be outside function definition/body
'''

# empty function

# def display():
#     pass

# display()

# def display():
#     print("welcome")

# display()
# print(type(display)) # function
# print(type(display())) # NoneType

# write function getdata()to take name and rollnumber from user.

# def getdata():
#     # getdata() # RecursionError: wrong way of called here
#     name = input("Enter name = ") 
#     rollnum = int(input("Enter rollnum = "))
#     print(name,rollnum)
#     getdata() # infinite called ownself/recursion    
# getdata()

# def show():
#     print("welcome")
#     show() # RecursionError: maximum recursion depth exceeded

# show()

# function with return

# def display():
#     print("welcome")
#     return # terminate block exection
#     print("python") # ignores this line
# display()

# def display():
#     return "welcome" # will notshow on console 

# display()
# print(display())

# def display():
#     return print("welcome") # not correct eay pf using print()
# display()
 
def display():
    a = 5
    b = 20
    add = a+b
    # reurn a+b
    return add

display()
print(display()/5)