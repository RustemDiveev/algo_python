from e2.CreditCard import PredatoryCreditCard

# TODO: Комментарии и тесты 
class PredatoryCreditCard_c29(PredatoryCreditCard):

    def __init__(
        self, customer, bank, acnt, limit, apr, 
        min_monthly_payment_pct, late_fee
    ):

        super().__init__(customer, bank, acnt, limit, apr)

        self.min_monthly_payment_pct = min_monthly_payment_pct
        self.late_fee = late_fee 

        self._month_begin_balance = 0
        self._month_customer_payment = 0

    @property 
    def min_monthly_payment_pct(self):
        return self._min_monthly_payment_pct 

    @min_monthly_payment_pct.setter
    def min_monthly_payment_pct(self, value):

        if not isinstance(value, (int, float)):
            raise ValueError("Минимальный месячный платеж должен быть числом.")

        if not 0 <= value <= 1:
            raise ValueError("Минимальный месячный платеж должен быть числом от 0 до 1.")

        self._min_monthly_payment_pct = value 

    @property 
    def late_fee(self):
        return self._late_fee 

    @late_fee.setter
    def late_fee(self, value):

        if not isinstance(value, (int, float)):
            raise ValueError("Штраф за просрочку должен быть числом.")

        if value < 0: 
            raise ValueError("Штраф за просрочку должен быть положительным числом.")

    def make_payment(self, amount):
        super().make_payment(amount)
        self._month_customer_payment += amount 

    
    def process_month(self):
        
        super().process_month()
        if self._month_customer_payment < self._month_begin_balance * self._min_monthly_payment_pct:
            self._balance += self.late_fee

        self._month_begin_balance = self._balance 
        self._month_customer_payment = 0
