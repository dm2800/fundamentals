
# USER CLASS CREATED WITH ATTRIBUTES + METHODS:
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
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    # DISPLAY USER BALANCE METHOD CREATED: 
    def display_user_balance(self):
        print(self.account_balance)
    # TRANSFER MONEY METHOD CREATED: 
    def transfer_money(self, amount, sender, recipient):
        sender.account_balance -= amount
        recipient.account_balance += amount


# 3 INSTANCES CREATED:
Danny = User("Danny Murcia", "dan@python.com")
Natasha = User("Natasha Murcia", "nat@python.com")
Pachito = User("Pachito McLekkerson", "pachi@python.com")


#FIRST USER:
Danny.make_deposit(100)
Danny.make_deposit(200)
Danny.make_deposit(300)
Danny.make_withdrawal(50)
Danny.display_user_balance()

#SECOND USER:
Natasha.make_deposit(1000)
Natasha.make_deposit(200)
Natasha.make_withdrawal(200)
Natasha.make_withdrawal(400)
Natasha.display_user_balance()

#THIRD USER:
Pachito.make_deposit(5000)
Pachito.make_withdrawal(100)
Pachito.make_withdrawal(50)
Pachito.make_withdrawal(50)
Pachito.display_user_balance()


#TRANSFER MONEY METHOD: 
Danny.transfer_money (200, Danny, Pachito)
Pachito.display_user_balance()
Danny.display_user_balance()
