# comprehension is replacement of traditional loop and also generatr result in sequence

# syntax:
# [expression(output) for i(iterable_variable) in ]

# print 1 to 5 using loop
# for i in range(1,6):
#     print(i, end=" ")

# print 1 to 5 using list comprehension
# [print(i) for i in range(1,6)]
# print([i for i in range(1,6)])

# ans = [i for i in range(1,6)]
# print(ans)

# WAP to show even and odd number from 1 to 10 using list comprehension

even = [i for i in range(2,11,2)]
print("even bunber = ",even)
odd = [i for i in range(1,11) if i%2 != 0]
print("odd number = ", odd)

# or
e,o = [],[]
[e.append(i) if i % 2 == 0 else o.append(i) for i in range(1,11)]
print("Even number",e)
print("odd number",o)

# WAP to show ebtred string by removeing vowel using list comprehension
# str = input("Enter string = ").lower()
# vowels = "aeiouAEIOU"
# ans = [i for i in str if i not in vowels ]
# print("".join(ans))

# str = input("Enter string = ").lower()
# ans = [i for i in str if i not in "aeiouAEIOU" ]
# print("".join(ans))

# WAP to print True for +ve and False for -ve number but take 10 number from user using list comprehension
number = [int(input(f"Enter {i} number = ")) for i in range(1,11)]
print(number)
ans = [True if i > 0 else False for i in number]
print(ans)