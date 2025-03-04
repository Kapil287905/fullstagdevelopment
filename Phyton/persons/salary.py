import emp
import days

def calculatesalary():
    perdaypay = 1000
    totalsalary = perdaypay * days.totaldays()
    print(f"Name = {emp.fullname()} and total salary = {totalsalary}")

calculatesalary()