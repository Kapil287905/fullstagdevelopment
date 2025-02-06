# WAP to show sum of digit of any 4 digit number positive interger number
n = int(input("Enter any 4 digit number = "))
sum = 0
n1 = n
rem1= n%10
n = n//10 
rem2= n%10
n = n//10 
rem3= n%10
n = n//10 
rem4= n%10
n = n//10 
sum=rem1+rem2+rem3+rem4
print(f"sum of digit of {n1} = {sum}")