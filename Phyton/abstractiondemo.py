# Abstraction:- It is way of hiding the implementation details and showing only
# the functionality to the user. i.e internal process will not be reveal to user
# there are two ways of representing abstraction 1) via localmathod 2) via ABC class->abstractmethod


# via localmathod
class ATM:
    def __init__(self,debitamount):
        self.balance = 10000
        self.debitamount = debitamount

    def getbalance(self):
        minbalance = 10000
        if self.balance-self.debitamount>=minbalance: 
            self.balance = self.balance-self.debitamount
            print("Amount debited successfully")
            print("Current Balance = ",self.balance)
        else:
            print("Insufficient balance")
            print("Current Balance = ",self.balance)

amount = float(input("Enter debit amount = "))
a = ATM(amount)
a.getbalance()
print("Minimum Balance = ",a.minbalance)