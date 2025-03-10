# methord: written by def blick and present onside class
# type of methord
# 1) local methord
# 2) @classmethod-decorator built-methord
# 3) @staticmethord-decorator built-methord
# 4) constructor method __init__(self) by default get called when object create

#local methord

"""
class Emp:
    officename = "Tata"

    def setdetails(self,name,jobprofile): # local methord
        self.name = name
        self.jobprofile = jobprofile

    def getdetails(self): # local methord
        print(f"name = {self.name},officename = {self.officename}, and jobprofile = {self.jobprofile}")

e=Emp()
e.setdetails("kpmal","data analyst")
e.getdetails()
print(e.name,e.jobprofile) # kpmal data analyst"

"""

# @classmethod

"""
class Emp:
    officename = "Tata"

    def setdetails(self,name,jobprofile): # local methord
        self.name = name
        self.jobprofile = jobprofile

    @classmethod
    def setofficename(cls):
        cls.officename = "TCS"

    def getdetails(self): # local methord
        # self.officename = "TCSION"
        print(f"object name = {self.name},officename = {self.officename}, and jobprofile = {self.jobprofile}")
        print(f"clsss name = {self.name},officename = {Emp.officename}, and jobprofile = {self.jobprofile}")
        print()

e=Emp()
e.setdetails("kpmal","data analyst")
e.getdetails()
# print(e.name,e.jobprofile) # kpmal data analyst"
e.setofficename() # @classmethood
e.getdetails()
Emp.officename = "Tata New"
e.getdetails()
"""

# @staticmethord

class Emp:
    officename = "Tata"

    def setdetails(self,name,jobprofile): # local methord
        self.name = name
        self.jobprofile = jobprofile

    @classmethod
    def setofficename(cls): # class method
        cls.officename = "TCS"

    def getdetails(self): # local methord
        # self.officename = "TCSION"
        print(f"object name = {self.name},officename = {self.officename}, and jobprofile = {self.jobprofile}")
        print(f"clsss name = {self.name},officename = {Emp.officename}, and jobprofile = {self.jobprofile}")
        print()

    @staticmethod
    def getsalary(salary): # no need to write self
        print("Salary = ",salary)

e=Emp()
e.setdetails("kpmal","data analyst")
e.getdetails()
# print(e.name,e.jobprofile) # kpmal data analyst"
e.setofficename() # @classmethood
e.getdetails()
Emp.officename = "Tata New"
e.getdetails()
e.setdetails("Raj","data engineer")
e.getsalary(80000)
e.getdetails()
Emp.getsalary(90000) # staticmethotd has been called via class
# Emp.getdetails() # error local methord are not callable by class