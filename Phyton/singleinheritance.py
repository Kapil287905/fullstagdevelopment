# Inheritance:-It is concept where single or many parent/child calss are their.
# but all child class can inherits all properties of parent class by default.

# single inheritance:- one parent and one child

class Person:
    def __init__(self,id):
        self.id = id

    def show(self):
        print(f"Person ID = {self.id}")

class student(Person):
    def __init__(self,id,name,degree):
        super().__init__(id)
        self.name = name
        self.degree = degree

    def show(self):
        print("Person as student")
        print(f"ID = {self.id},Name = {self.name},Degree = {self.degree}")

id = int(input("Enter ID = "))
name = input("Enter Name = ")
degree = input("Enter degree = ")
s=student(id,name,degree)
s.show()
p = Person(id) # no need to create object of perent as child is showing all property
p.show()