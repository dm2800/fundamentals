
#ASSIGNMENT: BANKACCOUNT

class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        # don't forget to add some default values for these parameters!
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon 
        self.int_rate = int_rate
        self.balance = balance
        int_rate = 0.01
        balance = 0
        # each instance is added to a list called all_accounts
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print('Balance: $' + str(self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0: 
            self.balance += (self.balance * self.int_rate)
            return self
        

Account1 = BankAccount(0.02, 1000)
Account2 = BankAccount(0.03, 2000)


Account1.deposit(200).deposit(100).deposit(400).withdraw(50).yield_interest().display_account_info()
Account2.deposit(100).deposit(100).deposit(100).deposit(500).withdraw(300).yield_interest().display_account_info()




