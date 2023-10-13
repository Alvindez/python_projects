from bankaccounts import *

Alvin = BankAccount(1600000, "Alvin")
Fify = BankAccount(2000000, "Fify")

Alvin.get_balance()
Fify.get_balance()

Alvin.deposit(500000)

Fify.withdraw(2100000)
Fify.withdraw(200000)