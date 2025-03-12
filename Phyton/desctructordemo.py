# Destructor:- It is called to when object get distory
# In python we don't need to call destructor because python call 
# automatically to handle memory via garbage collector. But we can use for debugging

'''
def __del__(self):
    stm
'''
# import keyword

# print(keyword.kwlist)
# print(keyword.iskeyword("del"))

# a = 10
# del a
# print(a)
class Emp:
    def __init__(self): # constructor
        print("init has called and Emp is created")

    def __del__(self): # destructor
        print("del i.e. destructor has called and Emp is distory")

e = Emp()
del e # no need to write automatically earlier line calls __del__