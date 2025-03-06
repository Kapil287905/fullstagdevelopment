# type of members in class
# 1) instance
# 2) static
# 3) local
# 4) class

# class Person:
#     id=1111 # class member

#     def getid(self):
#         id = 2222 # local member
#         print("id = ",id)

# t = Person()
# t.getid() # via method id=2222 local
# print("id = ",t.id) # id=1111 class
# print("id = ",Person.id) # id=1111 class
# print()

# Person.id = 5555
# t.getid() # 2222
# print("id = ",t.id) # 5555
# print("id = ",Person.id) # 5555
# print()

# t.id = 7777
# t.getid() # 2222
# print("id = ",t.id) # 7777
# print("id = ",Person.id) # 5555

# instance member can written by __init__(self) method
# ____init__(self) method is an default constructor which called every time when object created
# constructor method is invocation method it works when object create

'''
class Area:
    radius = 4.5 # calss member

    def __init__(self):
        self.length = 34 # instance member
        self.breadth = 56
        print(f"Area of Rectangle = {self.length*self.breadth}")

    def __init__(self):
        print("wellcome")
    
    def __init__(self,a,b):
       self.a=a
       self.b=b
       print(f"Addition = {self.a+self.b}")

    def circlearea(self):
        print(f"Area of Circle = {3.14*self.radius**2}")
    
    def __init__(self): # latest on will called because python dosen't support method
        print("Hello")
    
    def square(self,x):
        return x**2

a = Area() #__init__() method is calling here
# a = Area(4,5)
# a.__init__() # working but no need
a.circlearea()
print(a.square(5))
print(list(map(a.square,range(1,11))))
print(dir(Area))
# print(a.a,a.b) #init pameter won't be read
print(Area.a,Area.b)
print()'
'''

# sratic member
class student:
    rollnumber = 11 # class mwmber
    def __init__(self,grade):
        self.grade = grade # instance member
        self.name = "pooja" # instance member
        self.__address = "Malad"
        print(self.name,self.__address,self.grade)

    def show(self):
        percentage = 89.34 # local member
        __age = 28 # local member
        print(percentage,__age)

s = student("A")
s.show()
print(s.grade)
print(s.name)
# print(s.__address) #AttributeError: 'student' object has no attribute '_address'
print(s.percentage) # local method membor are not readable
print(s.__age) # local method membor are not readable
