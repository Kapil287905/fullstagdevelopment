from abc import ABC, abstractmethod

class car(ABC):
    @abstractmethod
    def mileage(self):
        print("Final abstract method")

    def show(self):
        print("local method")

# c = car() # TypeError: Can't instantiate abstract class car without an implementation for abstract method 'mileage'
# c.mileage() # won't work 
# c.show() # won't work 

class Tesla(car):
    def mileage(self):
        return super().mileage()
        
    def mile(self):
        print("Tesla has 90kmph mileage")

t = Tesla()
t.mileage()
t.mile()