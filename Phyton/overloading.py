# Python dosen't support function/method overloading

# function overloading
'''
def display():
    print("display-1")

# display()

def display(*args):
    print("dispaly-2")
    print(args)

def display(x,y):
    print("dispaly-3")
    print(x*y)

display("komal",1,"A") # TypeError: display() takes 2 positional arguments but 3 were given

display()'
'''

# function overloading doesn't support

class Demo:
    def display(self):
        print("display-1")

    def display(self,*args):
        print("dispaly-2")
        print(args)

    def display(self,x,y):
        print("dispaly-3")
        print(x*y)

d = Demo()
d.display() # TypeError: Demo.display() missing 2 required positional arguments: 'x' and 'y'