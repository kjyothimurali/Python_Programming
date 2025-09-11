"""You are asked to design a simple Payment System that can handle different payment methods.
Requirements:
Create a base class Payment with a method pay(amount).
Create three child classes that override the pay(amount) method:
CashPayment → print "Paid ₹<amount> in cash"
CardPayment → print "Paid ₹<amount> using credit/debit card"
UPIPayment → print "Paid ₹<amount> using UPI"
Task:
Create a list of payment objects (CashPayment, CardPayment, UPIPayment).
Loop through them and call pay(1000).
Each object should print a different message."""


from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amt):
        pass

class CashPayment(Payment):
    def pay(self,amt):
        print(f"Paid ₹{amt} in cash")


class CardPayment(Payment):
    def pay(self,amt):
        print(f"Paid ₹{amt} using credit/debit card")

class UPIPayment(Payment):
    def pay(self,amt):
        print(f"Paid ₹{amt} using UPI")

cash=CashPayment()
card=CardPayment()

upi=UPIPayment()
list_pays=[cash,card,upi]
for i in list_pays:
    i.pay(1000)