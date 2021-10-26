class CreditCard_c30:
    """
        CreditCard with protected setters and private class members
    """

    def __init__(self, customer, bank, acnt, limit):

        self.__customer = customer
        self.__bank = bank 
        self.__account = acnt
        self.__limit = limit 
        self.__balance = 0 

    @property 
    def customer(self):
        return self.__customer 

    @property 
    def bank(self):
        return self.__bank 

    @property 
    def account(self):
        return self.__account 

    @property 
    def limit(self):
        return self.__limit 

    @property 
    def balance(self):
        return self.__balance 

    def _set_balance(self, p_value):
        """
            Типа "защищенный" метод - сеттер баланса кредитной карты 
        """
        if not isinstance(p_value, (int, float)):
            raise ValueError("Баланс должен быть числом.")
        self.__balance = p_value 

    def charge(self, price):
        """
            Charge given price to card, assuming sufficient credit limit.
            Return True if charge was processed; False if charge was denied. 
        """
        if price + self.balance > self.limit:
            return False
        else:
            self._set_balance(self.balance + price) 
            return True

    def make_payment(self, amount):
        """
            Process customer payment that reduces balance.
        """
        self._set_balance(self.balance - amount)


class PredatoryCreditCard_c30(CreditCard_c30):
    """
        An extension to CreditCard that sets balance using protected method 
    """
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._set_balance(self.balance + 5)
        return success 

    def process_month(self):
        if self.balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor 
            monthly_factor = pow(1 + self._apr, 1/12)
            self._set_balance(self.balance * monthly_factor)
