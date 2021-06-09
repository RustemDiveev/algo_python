from e2.r6 import CreditCard_r6

class CreditCard_r7(CreditCard_r6):

    def __init__(self, customer, bank, acnt, limit, balance=0):
        super().__init__(customer, bank, acnt, limit)
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance of credit card must be a number.")
        if balance < 0:
            raise ValueError("Balance mustn't be a negative number.")
        self._balance = balance
