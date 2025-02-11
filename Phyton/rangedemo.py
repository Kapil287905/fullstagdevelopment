# range() used for showing number in sequence it must have below parameter
# start-optional (default-0)
# end-compulsory
# stop optional (default=1)

# print(range()) #error
# print(range(5)) #(0,4)
# print(list(range(5))) #[0, 1, 2, 3, 4]
# print(tuple(range(5)))
# print(set(range(5)))
# print(str(range(5))) #range(0, 5)
# # print(dict(range(5)))# error
# print(type(range))
# print(type(range(5)))
# # print(list(range("welcome"))) #error
# # print(list(range(2.34))) #error
# print(list(range(int(2.34)))) # range(0,2) [0, 1]
# print(list(range(int(True)))) # range(0,1) [0]

# WAP to print 1 to 10 number
print(list(range(1,11)))

# WAP to print even from 1 to 10 number
print(list(range(2,11,2)))

# WAP to print odd from 1 to 10 number
print(list(range(1,11,2)))

print(list(range(10,30,5))) #[10, 15, 20, 25]
print(list(range(30,10,5))) #[]
print(list(range(30,10,-5))) #[30, 25, 20, 15]
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(-5))) #[]
print(list(range(-5,0))) #[-5, -4, -3, -2, -1] start=-5 end=0 step1
print(list(range(-1,-6))) #[] start=-1 end=-6 step1
print(list(range(-1,-6,-1))) #[-1, -2, -3, -4, -5]
print(list(range(20,-0,-2)))
print(list(range(10,-5,-2))) #[10, 8, 6, 4, 2, 0, -2, -4]
print(list(range(1))) #[0]
print(list(range(1,0))) #[]
print(list(range(1,0,-1))) #[1]