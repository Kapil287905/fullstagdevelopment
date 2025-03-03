# variable writen inside function are called local variable
# global-variable writen outside function are called global variable
'''
def show():
    name = "raj"
    # pass

# peint(name) can't access outside
print(show())
'''

# a=10 #global
# def outer():
#     a=5 #local
#     print("Outer a = ", a)

#     def inner():
#         a=15
#         print("Inner a = ",a)
#     inner()
#     print("Outer inner a = ",a)

# outer()
# print("Outer outer a = ",a)

#convert local to global case-1 outer 

# a=10 #global
# def outer():
#     global a
#     a=5 
#     print("Outer a = ", a) #a=5

#     def inner():
#         a=15
#         print("Inner a = ",a) #a=15
#     inner()
#     print("Outer inner a = ",a) #a=5

# outer()
# print("Outer outer a = ",a) #a=5

#convert local to global case-1 (inner function)
# a=10 #global
# def outer():    
#     a=5 
#     print("Outer a = ", a) #a=5

#     def inner():
#         global a
#         a=15
#         print("Inner a = ",a) #a=15
#     inner()
#     print("Outer inner a = ",a) #a=5

# outer()
# print("Outer outer a = ",a) #a=15

# use of nonlocal scope

a=10 #global
def outer():
    # nonlocal a # not allowed here    
    a=5 
    print("Outer a = ", a) #a=5

    def inner():
        nonlocal a
        a=15
        print("Inner a = ",a) #a=15
    inner()
    print("Outer inner a = ",a) #a=15

outer()
print("Outer outer a = ",a) #a=10