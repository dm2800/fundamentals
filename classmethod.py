class BankAccount: 
    #class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance)
        self.int_rate = int_rate
        self.balance = balance
        # each instance is added to a list called all_accounts
        BankAccount.all_accounts.append(self)

# class method to change the name of the bank 
@classmethod
def change_bank_name(cls,name):
    cls.bank_name = name

# class method to get balance of all accounts 
@classmethod
def all_balances(cls):
    for account in cls.all_accounts:
        account.

# STATIC METHOD

class BankAccount: 
    def with_draw(self,amount):
        # we can use the static method here to evaluate 
        # if we can withdraw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount 
        else:
            print('Insufficient Funds')
        return self 
    # static methods have no access to any attribute
    # only to what is passed into it 
    @staticmethod 
    def can_withdraw(balance,amount)
        if (balance - amount) < 0: 
            return False 
        else: 
            return True

            





