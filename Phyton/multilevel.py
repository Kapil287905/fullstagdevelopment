# Multilevel
"""
A(Grand parent)

B(parent)

C(child)

"""

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

class Emp(student):
    def __init__(self, id, name, degree,jobprofile,salary):
        super().__init__(id, name, degree)
        self.jobprofile = jobprofile
        self.salary = salary

    def show(self):
        print("Emp as student")
        print(f"ID = {self.id},Name = {self.name},Degree = {self.degree},Jobprofile = {self.jobprofile},Salary={self.salary}")

id = int(input("Enter ID = "))
name = input("Enter Name = ")
degree = input("Enter degree = ")
job = input("Enter jobprofile = ")
salary = float(input("Enter salary = "))
# s=student(id,name,degree)
# s.show()
# p = Person(id) # no need to create object of perent as child is showing all property
# p.show()
e=Emp(id,name,degree,job,salary)
e.show()