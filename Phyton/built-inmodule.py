# built-in mobile

# import keyword
# print(dir(keyword)) # dir() show all methords and property
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(keyword.iskeyword("end")) # False
# print(keyword.iskeyword("for")) # True

# import math

# print(dir(math))
# print(math.factorial(5))
# print(math.floor(5.34536)) # trunctes decimal
# print(math.pi)
# print(math.remainder(77,4)) # 77%4
# print(math.ceil(7.56))
# print(math.sqrt(40))
# print(math.fabs(-7.5))

# import calendar

# print(dir(calendar))
# print(calendar.calendar(2025))
# print(calendar.month(2025,11))

# import datetime

# print(dir(datetime))
# print(datetime.datetime.now())
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)
# print(datetime.datetime.now().time())

# from datetime import datetime

# print(datetime.now().date())

# import random

# print(random.randrange(1,50))
# # print(random.randrange(12.35,14.3)) # TypeError: 'float' object cannot be interpreted as an integer
# print(random.randrange(1,50,2)) # only odd number
# print(random.randint(1,15)) # it don't have step
# print(random.choice(range(1,50)))
# name = "neel","sarim","kapil","tushar","ram"
# print(random.choice(name)) # return single element
# print(random.choices(name)) # return more than one id k-count 
# print(random.choices(name, k=2))
# print(random.sample(name, k=2))


# WAP to generate rendom password

# import string
# import random

# # allcharacters = string.ascii_letters + string.digits + string.punctuation
# allcharacters = string.ascii_letters + string.digits + "#$%_*&@"
# print(string.punctuation)
# length = int(input("enter length for password = "))
# password = "".join(random.choices(allcharacters,k=length))
# print("Your password = ",password)

# import os
# # print(dir(os))
# print(os.getcwd()) #current working directory
# print(os.listdir()) # show file and folder present inside
# # os.mkdir("dir") #create folder
# print(os.listdir())
# # os.rmdir("dir") #delete folder
# print(os.listdir())

import sys
# # print(dir(sys))
# # print(sys.path)
# print(sys.platform)
# print(sys.version)
# print(sys.version_info)
# print(sys.modules)

sys.stdout.write("welcome to myworld")
# command line argument only works with print()
print("enter your name = ",sys.argv)
print("fname = ",sys.argv[1])
print("lname = ",sys.argv[2])

