name = "kapil"
place = "mumbai"
print("My name is",name, "and I am from",place)

ans = "My name is",name, "and I am from",place
print(ans)

ans1 = f"My name is {name} and I am from {place}"
print(ans1)

# %s is string format specifier
ans3="My name is %s and I am from %s" %(name,place)
print(ans3)

ans4="My name is %s and I am from %s and %s" %(name,place,"delhi")
print(ans4)

ans5="My name is {0} and I am from {1}" .format(name,place)
print(ans5)

per=98.78965432
ans6 = f"My name is {name} and I am from {place} and I got {per:0.2f} percentagr"
print(ans6)