# slicing of string [start:end:step]
# Rules
# srart:- optional and default 0
# end:- optional and default lasr char if specified rhem it skip end and stop before 2nd last
# step:- optional and default +1

data = "welcome"
# print(data[:]) # welcome
# print(data[::]) # welcome
# print(data[3:]) # come
# print(data[:3]) # wel
# print(data[::3]) # wce

# print(data[-3:]) # ome
# print(data[:-3]) # welc
# print(data[::-3]) # ecw start from -1
# print(data[0:1]) # w
print(data[-3:3]) # empty
print(data[0::]) # welcome
print(data[-1::]) # e
print(data[:-1:]) # welcom
print(data[::-1]) # emoclew reverse of string