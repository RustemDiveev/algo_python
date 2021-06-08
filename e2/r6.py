from e2.r5 import CreditCard_r5

class CreditCard_r6(CreditCard_r5):

    def make_payment(self, amount):
        if isinstance(amount, (int, float)) and amount < 0:
            raise ValueError("Amount during making payment must be posiive number")
        super().make_payment(amount)
