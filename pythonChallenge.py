class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposite(self, amount):
        print("Deposite Accepted")

    def withdraw(self, amount):
        if amount < 500:
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposite(50)
acct1.withdraw(50)
acct1.withdraw(500)
