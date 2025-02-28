# Tuper of argument
# 1)positional(*)
# 2)keyword(**)

# 1) (*args)- non keyword argument where we can give nth number of argument
# case-1
# def studentdata(*args):
#     print(args)
#     print("ID = ",args[0])
#     print("Name = ",args[1])
#     # print("Grade = ",args[2])

# studentdata(1,"riya","A")
# studentdata(1,"riya")

# case-2
# def studentdata(id, *args):
#     print(args)
#     print("ID = ",id)
#     print("Name = ",args[0])
#     print("Grade = ",args[1])

# studentdata(101,"komal","A+")

# case-3
def studentdata(id, *args):
    # print("ID = ",id)
    # print(f"{id} student detail = {args}")
    print(f"{id} student detail: ")
    for i in args:
        print(i, end=" ")
    

studentdata(101,"komal","A+","Mumbai","India")
# studentdata(102,"priti","Mumbai","India")
# studentdata(103)