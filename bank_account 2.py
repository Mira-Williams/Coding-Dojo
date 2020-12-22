
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        return self
    
account_1 = BankAccount(0.05, 1000)
account_2 = BankAccount(0.03, 1500)

account_1.deposit(1234).deposit(124).deposit(134).withdraw(876).yield_interest()
account_2.deposit(567).deposit(507).withdraw(823).withdraw(82).withdraw(23).withdraw(83).yield_interest()

account_1.display_account_info()
account_2.display_account_info()

# def __init__(self, int_rate, balance=0):
#     self.int_rate = int_rate
#     self.balance = balance