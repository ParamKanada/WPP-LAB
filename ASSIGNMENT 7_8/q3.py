# Bank

class bankacc:

    def __init__(self, accnumber, accholder, balance=0.0):
        self.accnumber = accnumber
        self.accholder = accholder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.accnumber} , New balance: {self.balance}\n")
        else:
            print("Invalid Operation !!!\n")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.accnumber} , New balance: {self.balance}\n")
        elif amount > self.balance:
            print("Insufficient balance !\n")
        else:
            print("Invalid Operation")

    def getbalance(self):
        return self.balance

    def displaydetails(self):
        print(f"Account Number: {self.accnumber}\nAccount Holder: {self.accholder}\nBalance: {self.balance}\n")

class bank:
    
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def createaccount(self, accnumber, accholder, initialbalance=0.0):
        if accnumber in self.accounts:
            print("Account number already exists !\n")
        else:
            self.accounts[accnumber] = bankacc(accnumber, accholder, initialbalance)
            print(f"Account for {accholder} created successfully \n")

    def getaccount(self, accnumber):
        return self.accounts.get(accnumber, None)

    def deposit(self, accnumber, amount):
        account = self.getaccount(accnumber)
        if account:
            account.deposit(amount)
        else:
            print("Account not found !!!\n")

    def withdraw(self, accnumber, amount):
        account = self.getaccount(accnumber)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found !!!\n")

    def displayaccounts(self):
        if not self.accounts:
            print("No accounts found !!!\n")
        else:
            print(f"\nAccounts in {self.bank_name}:")
            for account in self.accounts.values():
                account.displaydetails()
                print("-" * 30)

o = input("Enter bank name = \n")
a = bank(o)

b = int(input("Enter Acc Number = \n"))
c = input("Enter Acc Holder Name = \n")
d = int(input("Enter Acc balance = \n"))

a.createaccount(b,c,d)

e = int(input("Enter How much you wanna deposit = \n"))
a.deposit(b,e)

f = int(input("Enter How much you wanna withdraw = \n"))
a.withdraw(b,f)

print("\nDisplay...\n")
a.displayaccounts()