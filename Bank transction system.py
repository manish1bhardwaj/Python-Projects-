# 6. Problem: Bank Transaction System 
# Description: Build a BankAccount class with methods for deposit, withdraw, and check 
# balance.

class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
    def deposit(self, amount): 
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    def withdraw(self, amount):   
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds in the account.")
        self.balance -= amount
    def get_balance(self):   
        return self.balance
    def __str__(self):  
        return f"BankAccount({self.account_number}, Owner: {self.owner}, Balance: {self.balance})"

# Example Usage
account = BankAccount("123456789", "John Doe", 1000)
print(account)

account.deposit(500)
print("After deposit:", account.get_balance())

account.withdraw(200)
print("After withdrawal:", account.get_balance())