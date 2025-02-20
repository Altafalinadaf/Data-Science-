class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #private attribute

    def deposite(self,amount):
        self.__balance+=amount
    
    def get_balances(self):
        return self.__balance

account = BankAccount(1000)
account.deposite(500)
print(account.get_balances())