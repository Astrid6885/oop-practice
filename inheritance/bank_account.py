"""Inheritance - Problem 3: BankAccount and SavingsAccount."""


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("The amount must be positive.")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("The amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        return True

    def transfer(self, amount, destination):
        # Move money to another account.
        # Returns False if the balance is not enough, True otherwise.
        if self.withdraw(amount):
            destination.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account {self.account_number}: {self.balance:.2f} EUR"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # e.g. 0.03 means 3%

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    current = BankAccount("FR-001", 500)
    savings = SavingsAccount("FR-002", 1000, interest_rate=0.05)

    print(current)
    print(savings)

    print("Transfer 200 to savings:", current.transfer(200, savings))   # True
    print("Transfer 1000 to savings:", current.transfer(1000, savings)) # False

    print("Interest added:", savings.add_interest())  # 1200 * 0.05 = 60.0
    print("Savings balance:", savings.check_balance())  # 1260.0
    print(current)
