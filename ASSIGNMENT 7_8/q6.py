# bank Acc

class bankacc:

    def __init__(self, accnumber, accholder, balance=0.0):
        self.accnumber = accnumber
        self.accholder = accholder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.accnumber}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.accnumber} , New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def getbalance(self):
        return self.balance

    def displaydetails(self):
        print(f"Account Number: {self.accnumber}\nAccount Holder: {self.accholder}\nBalance: {self.balance}")

b = int(input("Enter Acc Number = \n"))
c = input("Enter Acc Holder Name = \n")
d = int(input("Enter Acc balance = \n"))

a = bankacc(b,c,d)

e = int(input("Enter How much you wanna deposit = \n"))
a.deposit(e)

f = int(input("Enter How much you wanna withdraw = \n"))
a.withdraw(f)

print("\nDisplay...\n")
a.displaydetails()