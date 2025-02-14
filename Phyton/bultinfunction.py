# Built-in function for string
"""
print(len("welcome"))
print(len("welcome python"))
# print(len(123)) #TypeError: object of type 'int' has no len()
print(len(str(123)))
print(ord("A")) #65 ASCII code
# print(ord("Anu")) #error
print(chr(97)) #a
print(min("python")) #h
print(max("python")) #y
print(max("343453python hi")) #y
# print(max("1234")) #error
print(sorted("python")) # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted("python")[::]) # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted("python")[::-1]) # ['y', 't', 'p', 'o', 'n', 'h']

"""

# oprations on string
x = "python"
y = "java"

print(x+y) #concatenation
# print(x-y) #error
# print(1234 + "welcome") #error
# print(x/y) #error
# print(x * y) #error
print(x * 3) #repeats string 3 time
print(x * True) # python
print(x * False) # empty
print("10" * 10)
a = "10"
print(int(a) * 10)
print(x > y) # first chat of ascii code
print(x == y) # false
print(x is y) # false
print("p" in y) # false
msg = "hi hello"
print(" " in msg) # true