import random

class bank:
    def __init__(self, name, acc_num, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Deposited amount be positive")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdrawal amount must be positive and cant be zero")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def showbalance(self):
        print(f"Your current balance is {self.balance}")
        
    def account_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Number: {self.acc_num}")
        print(f"Account Balance: {self.balance}")


def main():
    print("Wellcome to MyBank")
    acc_num = random.randrange(100000000000, 999999999999)
    name = input("Enter Account holder name: ")
    b = bank(name,acc_num)
    
    while True:
        print("--------Bank menu--------")
        print("1:Deposit\n2:Withdraw\n3:Check Balance\n4:Account Detail\n5:Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter deposit amount = "))    
            b.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdraw amount = "))    
            b.withdraw(amount)
        elif choice == "3":
            b.showbalance()
        elif choice == "4":
            b.account_details()
        elif choice == "5":
            print("Thank you for using our service")
            break
        else:
            print("Invalid choice number")


if __name__ == "main":
    main()
        