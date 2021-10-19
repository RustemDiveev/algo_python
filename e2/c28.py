from datetime import date 
from e2.CreditCard import PredatoryCreditCard 
            
def get_current_year_and_month():
    """
        Helper
        Returns tuple with current month and year 
    """
    l_today = date.today()
    return (l_today.month, l_today.year)

class CreditCard_c28(PredatoryCreditCard):
    """
        Modified PredatoryCreditCard, that once a customer made ten calls to charge in current month 
        - each additional call to charge results in $1 additional subcharge 
    """
    def __init__(self, customer, bank, acnt, limit, apr):
        """
            Creates a new predatory credit card instance.
            The initial balance is zero.

            customer    the name of the customer (e.g., 'John Bowman')    
            bank        the name of the bank (e.g., 'California Savings')
            acnt        the account identifier (e.g., '5391 0375 9387 5309')
            limit       credit limit (measured in dollars)            
            apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit, apr)
        self._currentperiod = get_current_year_and_month()
        self._calls_to_charge_cnt = 0

    def charge(self, price):
        """
            Charge given price to the card, assuming sufficient credit limit.

            Return True if charge was processed. 
            If there were more than 10 calls in current month charges with $1 surcharge.
            Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)
        l_current_period = get_current_year_and_month()
        if l_current_period[0] > self._currentperiod[0] \
            or l_current_period[1] > self._currentperiod[1]:
            self._currentperiod = get_current_year_and_month()
            self._calls_to_charge_cnt = 0
        else:
            self._calls_to_charge_cnt += 1
            if self._calls_to_charge_cnt > 10:
                self._balance += 1
        return success 
