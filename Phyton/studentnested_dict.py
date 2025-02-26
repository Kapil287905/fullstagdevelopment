# count = int(input("Enter cpount fpr student = "))
# studentdb = {}
# for i in range(count):
#     sid=int(input(f"Enter {i+1} student sid = "))
#     name=input(f"Enter {i+1} student name = ")
#     per=float(input(f"Enter {i+1} student per = "))
#     grade=input(f"Enter {i+1} student grade = ")
#     data = {sid:{"Name":name,"percentage":per,"Grade":grade}}
#     studentdb.update(data)

# print(studentdb)
# print("-------Student Details-------")
# print("SID Name Percentage Grade")
# for k,v in studentdb.items():
#     print(k, end=" ")
#     for i in v.values():
#         print(i, end=" ")
#     print()

# studentdata = {
#     "sid":[101,102],
#     "name":["raj","pooja"],
#     "percentage":[89,79],
#     "grade":["A","B"]
# }

# for k,v in studentdata.items():
#     print(k,v)
# # find 102 records
# print("Sid = ", studentdata["sid"][1])
# print("Name = ", studentdata["name"][1])
# print("Percentage = ", studentdata["percentage"][1])
# print("Grade = ", studentdata["grade"][1])

# -------------or

count = int(input("Enter cpount fpr student = "))
studentdb = {}
allsid = []
allname = []
allpercentage = []
allgrade = []
for i in range(count):
    sid=int(input(f"Enter {i+1} student sid = "))
    name=input(f"Enter {i+1} student name = ")
    per=float(input(f"Enter {i+1} student per = "))
    grade=input(f"Enter {i+1} student grade = ")
    # data = {sid:{"Name":name,"percentage":per,"Grade":grade}}
    allsid.append(sid)
    allname.append(name)
    allpercentage.append(per)
    allgrade.append(grade)
    data = {
        "sid":allsid,
        "name":allname,
        "percentage":allpercentage,
        "grade": allgrade

    }
    studentdb.update(data)

print(studentdb)
print("-------Student Details-------")
print("SID Name Percentage Grade")
for k,v in studentdb.items():
    print(k," = ",v)
    