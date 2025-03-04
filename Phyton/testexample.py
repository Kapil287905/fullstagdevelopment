n = 6

for i in range(1,6):
    if i % 2 == 0:
         print("o")
    else:    
        for j in range(1,6):
            if j % 2 == 0:
                print("o",end=" ")
            else:
                print("x",end=" ")

print()
