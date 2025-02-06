try:
    count = int(input("Enter count of student= "))
    i = 1
    while i <= count:
        rollnum = int(input("Enter roll number= "))
        name = input(f"Enter {rollnum} name= ")
        py = int(input(f"Enter {rollnum} python marks= "))
        sql = int(input(f"Enter {rollnum} sql marks= "))
        js = int(input(f"Enter {rollnum} js marks= "))
        css = int(input(f"Enter {rollnum} css marks= "))
        html = int(input(f"Enter {rollnum} html marks= "))
        if py>=0 and py<=100 and sql>=0 and sql<=100 and js>=0 and js<=100 and css>=0 and css<=100 and html>=0 and html<=100:
            totalmarks = py + sql + js + css + html
            print(f"Total marks of {rollnum} = {totalmarks}")
            pre = totalmarks/5
            print(f"Percentage  of {rollnum} = {pre} ")
        else:
            print("check entered marks of all subject. Marks sure that all marks are less than or equal 100 or can't be negative")
        i+=1
except:
    print("invalid input")