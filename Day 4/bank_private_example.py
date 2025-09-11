class BankAccount:
    __balance=0
    def deposit(self,amt):
        self.__balance=self.__balance+amt

    def withdraw(self,amt):
        if amt<self.__balance:
            self.__balance=self.__balance-amt
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    

bankacc=BankAccount()
#print(bankacc.__balance) --->error private variable accessing
print("depositing 5000")
bankacc.deposit(5000)
print("withdrawing 2000")
bankacc.withdraw(2000)
print(f"Current Balance : {bankacc.get_balance()}")