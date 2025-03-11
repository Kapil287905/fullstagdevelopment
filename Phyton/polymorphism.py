# polymorphism:= poly means many and morph means form
# so all together we call polymorphism means "many forms". it allow us single
# action to perform in different way via inheritance.
# it also called as methord overriding.
# It is works under parent and child(Inheritance)

class Grandparent:
    def showmobile(self):
        print("Grandparent have iphone=11")

class Parent:
    def showmobile(self):
        print("Grandparent have iphone=13")

class Child:
    def showmobile(self):
        print("Grandparent have iphone=16")

c = Child()
c.showmobile()  
p = Parent()
p.showmobile()  
g = Grandparent()
g.showmobile()        