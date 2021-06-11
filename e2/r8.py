import sys
sys.path.append("C:\IT\python\\algo\\algo_python")

from e2.r5 import CreditCard

def test_credit_card(p_int: int) -> tuple:
    wallet = []
    wallet.append(
        CreditCard(
            'John Bowman',
            'California Savings',
            '5391 0375 9387 5309',
            2500
        )
    )
    wallet.append(
        CreditCard(
            'John Bowman',
            'California Federal',
            '3485 0399 3395 1954',
            3500
        )
    )
    wallet.append(
        CreditCard(
            'John Bowman',
            'California Finance',
            '5391 0375 9387 5309',
            5000
        )
    )

    # Third card exceeds it's credit limit, while the first two are not
    for val in range(1, p_int):
        l_limit_exceeded_0 = wallet[0].charge(val)
        l_limit_exceeded_1 = wallet[1].charge(2*val)
        l_limit_exceeded_2 = wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()

    return (l_limit_exceeded_0, l_limit_exceeded_1, l_limit_exceeded_2)

for i in range(2, 60):
    l = test_credit_card(p_int=i)
    if (l[0] is True and l[1] is True and l[2] is False) or \
        (l[1] is True and l[2] is True and l[0] is False) or \
        (l[0] is True and l[2] is True and l[1] is False):
        print('Perfect value is =', i)
        break
