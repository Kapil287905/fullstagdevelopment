# Empty class
# class person:
#     pass

# p = person() # Object
# print(type(person)) # <class 'type'>
# print(type(p)) # <class '__main__.person'>
# print(dir(person)) # __init__(constructor method),__new__ dunder or magic method

class Person:
    name = "pooja"
    # print("Welcome",name)

Person
p = Person()
# print(p) # <__main__.Person object at 0x000001D6C3CA6A50>
print("Good morning",p.name)
print("Hello",Person.name)