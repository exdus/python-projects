class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.minimum_balance=500

    def deposit(self, amount):
        #self.balance += amount
            if amount < 0:
                print("Invalid deposit")
            else:
                self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if a1.balance < self.minimum_balance:
                print("cannot withdraw beyond the minimum account balance")
        elif a1.balance < self.minimum_balance:
                print("cannot withdraw beyond the minimum account balance")
        elif amount < 0:
            print("Invalid Withdrawal amount")
 
        else:
                self.balance-=amount
        
a1=Account("john","",200)
a1.deposit(1000000)
a1.withdraw(56000)


class currentAccount(Account):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if a1.balance < self.minimum_balance:
                print("cannot withdraw beyond the minimum account balance")
        elif a1.balance < self.minimum_balance:
                print("cannot withdraw beyond the minimum account balance")
        elif amount < 0:
            print("Invalid Withdrawal amount")
 
        else:
                self.balance-=amount
                
print a1.balance
