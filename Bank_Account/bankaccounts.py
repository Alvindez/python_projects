class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount {self.name} created. \nBalance = UGshs{self.balance}")