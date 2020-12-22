
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

mike = User("Mikey", "mikey@gmail.com")
mike.make_deposit(100).make_deposit(150).make_deposit(200).make_withdrawal(50).display_user_balance()

eric = User("Eric", "ericthered@gmail.com")
eric.make_deposit(1).make_deposit(1).make_withdrawal(100).make_withdrawal(100).display_user_balance()

tony = User("Tony", "eytonay@gmail.com")
tony.make_deposit(1000).make_withdrawal(-1000).make_withdrawal(-1000).make_withdrawal(-1000).display_user_balance()


