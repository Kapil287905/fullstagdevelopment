class College:
    id = 1111
    name = "ruparel"
    address = "matunga"

    def show(self): # self used refer class
        print(self.id,self.name,self.address)

print(College.id,College.name,College.address) # 1111
c1 = College()
print(c1.id,c1.name,c1.address) # 1111
print()
College.id = 5555
print(College.id,College.name,College.address) # 5555
print(c1.id,c1.name,c1.address) # 5555
print()
c1.id = 7777
print(College.id,College.name,College.address) # 5555
print(c1.id,c1.name,c1.address) # 7777
print()
# College.show()
c1.show()