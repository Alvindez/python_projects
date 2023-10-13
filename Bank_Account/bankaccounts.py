class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount {self.name} created. \nBalance = UGshs{self.balance}")

    def get_balance(self):
        print(f"\nAccount {self.name} \nbalance = UGshs{self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Cmplete.")
        self.get_balance()