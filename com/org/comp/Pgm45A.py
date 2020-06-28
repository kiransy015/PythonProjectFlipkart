class Bank:
    bank_balance=100000

class Account:
    def __init__(self,amt):
        self.account_balance = amt

    def deposit(self,amt):
        Bank.bank_balance=Bank.bank_balance+amt
        self.account_balance=self.account_balance+amt

    def withdraw(self,amt):
        Bank.bank_balance=Bank.bank_balance-amt
        self.account_balance = self.account_balance-amt

    def display_info(self):
        print("---------------------")
        print("Customer balance is=",self.account_balance)
        print("Bank balance is=",Bank.bank_balance)

print("------------Customer1------------")
c1 = Account(30000)
c1.display_info()
c1.withdraw(20000)
c1.display_info()

print("------------Customer2------------")
c2 = Account(100000)
c2.withdraw(50000)
c2.display_info()

print("------------Customer3------------")
c3 = Account(3000000)
c3.display_info()
c3.withdraw(1000000)
c3.display_info()
print("---------------------------------")