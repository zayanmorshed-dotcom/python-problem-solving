from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} BDT using Cash.")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} BDT using Card.")

p1 = CashPayment()
p1.pay(5000)

p2 = CardPayment()
p2.pay(3000)
