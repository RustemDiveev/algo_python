from datetime import date, datetime, timedelta
from random import randrange

def generate_birthday() -> datetime:
    """
        Generates random birthday from 2020-01-01 to 2020-12-31
    """
    l_start_date = date(2020, 1, 1)
    l_random_day = randrange(start=0, stop=364)
    l_random_date = l_start_date + timedelta(days=l_random_day)
    return l_random_date
    
