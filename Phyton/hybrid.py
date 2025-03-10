# Hybrid
'''
        A(vehicle)
--------------------------
B(two)              C(foue)
---------------------------
      D(customer)
'''

class Vehicle:
    def __init__(self,companyname):
        self.companyname = companyname

class twowheeler(Vehicle):
    def __init__(self, companyname,t_Vehiclename,t_modulenum):
        self.companyname = companyname       
        self.t_Vehiclename = t_Vehiclename
        self.t_modulenum = t_modulenum

    def twowheelerdata(self):
        print("Two wheeler vehicle company name = ",self.companyname)
        print("Two wheeler vehicle name =",self.t_Vehiclename)
        print("Two wheeler vehicle module number =",self.t_modulenum)

class fourwheeler(Vehicle):
    def __init__(self, companyname,f_Vehiclename,f_modulenum):
        self.companyname = companyname       
        self.f_Vehiclename = f_Vehiclename
        self.f_modulenum = f_modulenum

    def fourwheelerdata(self):
        print("Four wheeler vehicle company name = ",self.companyname)
        print("Four wheeler vehicle name =",self.f_Vehiclename)
        print("Four wheeler vehicle module number =",self.f_modulenum)

class customers(twowheeler,fourwheeler):
    def __init__(self, companyname, t_Vehiclename, t_modulenum, f_Vehiclename, f_modulenum,name,licnum):
        # super().__init__(companyname, t_Vehiclename, t_modulenum)
        self.companyname = companyname
        self.t_Vehiclename = t_Vehiclename
        self.t_modulenum = t_modulenum
        self.f_Vehiclename = f_Vehiclename
        self.f_modulenum = f_modulenum
        self.name = name
        self.licnum = licnum

    def customerdetail(self):
        print("customer Name = ",self.name, "\nLicense Number = ",self.licnum)
        print("--------Vehicle Setail--------")
        print("Company name = ",self.companyname)
        print("Two wheeler vehicle name =",self.t_Vehiclename)
        print("Two wheeler vehicle module number =",self.t_modulenum)
        print("Four wheeler vehicle name =",self.f_Vehiclename)
        print("Four wheeler vehicle module number =",self.f_modulenum)



# companyname = input("Enter company name =")
# Vehiclename = input("Enter vehicle name =")
# modulenum = input("Enter vehicle modle number =")
# f = fourwheeler()
# f.fourwheelerdata()
# t = twowheeler("Tata","tzp",1111)
# t.twowheelerdata(companyname.Vehiclename,modulenum)
# t = twowheeler("Tata","tzp",1111)
# t.twowheelerdata()
c = customers("Tata","tzp",1111,"four",1111,"komal",234234252)
c.customerdetail()