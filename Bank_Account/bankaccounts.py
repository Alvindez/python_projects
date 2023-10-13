class BalanceException(Exception):
    pass

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

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {self.name} only has a balance of UGshs{self.balance}")
    

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.get_balance()

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")