
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

mike = User("Mikey", "mikey@gmail.com")
mike.make_deposit(100)
mike.make_deposit(150)
mike.make_deposit(200)
mike.make_withdrawal(50)
mike.display_user_balance()

eric = User("Eric", "ericthered@gmail.com")
eric.make_deposit(1)
eric.make_deposit(1)
eric.make_withdrawal(100)
eric.make_withdrawal(100)
eric.display_user_balance()

tony = User("Tony", "eytonay@gmail.com")
tony.make_deposit(1000)
tony.make_withdrawal(-1000)
tony.make_withdrawal(-1000)
tony.make_withdrawal(-1000)
tony.display_user_balance()


