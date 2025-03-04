# type1
# import module1

# print(module1.msg)
# print(module1.addition(56,67))

# type2
# from module1 import addition
# print(addition(4,5))
# # print(module1.msg) #error

# type3
# from module1 import *
# print(msg)
# show()
# print(100 + addition(4,45))

# type4

from module1 import addition as a
import module1 as m1

print(a(45,100))
print(m1.addition(45,100))