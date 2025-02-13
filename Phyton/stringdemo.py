# string=set of literal and endclosed within an quotes(single,double,triple)
# it is also call sequance

#empty string

# s=""
# print(type(s),s)

# s="Python"
# print(type(s),s)

# s="4234234234"
# print(type(s),s)

# s="all # 26542 5364"
# print(type(s),s)

# s="a"
# print(type(s),s)

# name = input("Enter name = ")
# print(type(name),name)

# per = 45.546
# print(type(per),per)

# newper = str(per)
# print(type(newper),newper)

# Accessing / reading string element via index
data = "python"
print(data)

#positive index with start 0 left side
# print("first char = ",data[0])
# print("2nd char = ",data[1])
# print("length = ",len(data))
# print("Middle char =",data[len(data)//2])
# print("last char = ",data[len(data)-1])
# print("2nd lasr char = ",data[len(data)-2])

#Negative index with start -1 from right side
print("last char = ",data[-1])
print("2nd lasr char = ",data[-2])
print("first char = ",data[-len(data)])
print("2nd char = ",data[-len(data) + 1])
print("Middle char =",data[-len(data)//2])