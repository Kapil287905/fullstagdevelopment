# Encapsulation:- It is a mechanism of building data member and methods together
# to hides from the class. It can be defined as packing of data and method into one component

class car:
    def __init__(self,model,price,speed):
        self.model=model
        self.price=price
        self.speed=speed

    def showmodel(self):
        print("Car model = ",self.model)

    def shoprice(self):
        print("Car price = ",self.price)

    def showspeed(self):
        print("Car speed = ",self.speed)

c = car("Honda123",90000,8700)
c.showmodel()