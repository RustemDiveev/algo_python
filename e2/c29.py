from e2.CreditCard import PredatoryCreditCard


class PredatoryCreditCard_c29(PredatoryCreditCard):

    def __init__(
        self, customer: str, bank: str, acnt: str, limit: float, apr: float, 
        min_monthly_payment_pct: float, late_fee: int
    ):
        """
            Конструктор класса 
            input:
                customer    - ФИО клиента 
                bank        - название банка 
                acnt        - 16значный номер счета 
                limit       - сумма лимита на кредитной карте 
                apr         - годовая процентная ставка 
                min_monthly_payment_pct - процент от баланса, 
                который держатель кредитной карты должен ежемесячно оплачивать
                late_fee    - величина штрафа, 
                которую платит держатель, если не выплатил минимальный ежемесячный платеж 
        """

        super().__init__(customer, bank, acnt, limit, apr)

        self.min_monthly_payment_pct = min_monthly_payment_pct
        self.late_fee = late_fee 

        # Баланс на начало месяца 
        self._month_begin_balance = 0
        # Сумма платежей (погашений) кредита держателем за месяц 
        self._month_customer_payment = 0

    @property 
    def min_monthly_payment_pct(self):
        """
            Возвращает процент от баланса, который необходимо оплачивать за месяц 
        """
        return self._min_monthly_payment_pct 

    @min_monthly_payment_pct.setter
    def min_monthly_payment_pct(self, value):
        """
            Устанавливает значение процента от баланса для обязательного погашения 
            каждый месяц 
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Минимальный месячный платеж должен быть числом.")

        if not 0 <= value <= 1:
            raise ValueError("Минимальный месячный платеж должен быть числом от 0 до 1.")

        self._min_monthly_payment_pct = value 

    @property 
    def late_fee(self):
        """
            Штраф за непогашение минимального месячного платежа 
        """
        return self._late_fee 

    @late_fee.setter
    def late_fee(self, value):
        """
            Устанавливает штраф за непогашение миинимального месячного платежа 
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Штраф за просрочку должен быть числом.")

        if value < 0: 
            raise ValueError("Штраф за просрочку должен быть положительным числом.")

        self._late_fee = value 

    def make_payment(self, amount):
        """
            Платеж держателя карты по кредиту 
            Накапливаем сумму всех погашений за месяц 
        """
        super().make_payment(amount)
        self._month_customer_payment += amount 

    
    def process_month(self):
        """
            Расчет всех штрафов по окончании платежного периода (конец месяца)
        """
        super().process_month()
        # Был ли погашен ежемесячный платеж
        if self._month_customer_payment < self._month_begin_balance * self._min_monthly_payment_pct:
            self._balance += self.late_fee

        # Обновляем баланс на начало месяца и сумму оплат по кредиту 
        self._month_begin_balance = self._balance 
        self._month_customer_payment = 0
