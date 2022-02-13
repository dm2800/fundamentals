class User: 
    pass 

michael = User()
anna = User()


class User: 
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has 2 parameters: 
    def __init__(self, name, email_address): 
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")


guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.account_balance)
print(monty.account_balance)




# print(guido.name)
# print (monty.name)




# User.bank_name = "Bank of Dojo"




# print(guido.bank_name)
# print(monty.bank_name)

# print(guido.name)
# print (monty.name)

# guido.name = "Guido"
# print(guido.name)
# monty.name = "Monty"
# print(monty.name)

