students = [["id","name","grade"],[1,"Raj","A"],[2,"Komal","B"]]
# print(students)
# print(len(students))
# print(students[0])
# print(students[1])
# print(students[2])
# for i in students:
#     print(i)

# find student name and grade whose id id 2
# print("student id 2 name is = ",students[2][1])
# print("student id 2 grade is = ",students[2][2])

# for i in range(len(students)):
#     for j in range(len(students)):
#         print(students[i][j], end="\t")
#     print()

# for i in students:
#     for j in i:
#         print(j, end="\t")
#     print()

# find student name and grade for entred id by user
print("search by id = ")
id = int(input("enter id to find bane and grade = "))
flag = False
for i in students:
    if i[0] == id:
        flag = True
        print("ID = ", i[0])
        print("Name = ",i[1])
        print("Grade = ",i[2])
        
if flag == False:
    print("id not found")