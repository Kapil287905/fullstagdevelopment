# hierarical
'''
      A
---------------
D              E
'''

class Vehicle:
    companyname = input("Enter company name = ")

class twowheeler(Vehicle):
    t_Vehiclename = input("Enter two wheeler vehicle name = ")
    t_modulenum = input("Enter two wheeler module number = ")

    def twowheelerdata(self):
        print("Two wheeler vehicle company name = ",self.companyname)
        print("Two wheeler vehicle name =",self.t_Vehiclename)
        print("Two wheeler vehicle module number =",self.t_modulenum)

class fourwheeler(Vehicle):
    Vehiclename = input("Enter four wheeler vehicle name = ")
    modulenum = input("Enter four wheeler module number = ")

    def fourwheelerdata(self):
        print("Four wheeler vehicle company name = ",self.companyname)
        print("Four wheeler vehicle name =",self.Vehiclename)
        print("Four wheeler vehicle module number =",self.modulenum)
        
# f = fourwheeler()
# f.fourwheelerdata()
f = twowheeler()
f.twowheelerdata()
