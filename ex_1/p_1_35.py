from datetime import date, datetime, timedelta
from random import randrange
from collections import Counter

def generate_birthday() -> datetime:
    """
        Returns random birthday from 2020-01-01 to 2020-12-31
        output:
            random date 
    """
    l_start_date = date(2020, 1, 1)
    l_random_day = randrange(start=0, stop=364)
    l_random_date = l_start_date + timedelta(days=l_random_day)
    return l_random_date

def generate_birthdays(p_amount: int) -> list:
    """
        Returns list of random birthdays
        input:
            p_amount - generated birthday count
        output:
            list of generated birthdays
    """
    l_result = []
    for i in range(p_amount):
        l_result.append(generate_birthday())
    return l_result

def count_birthdays(p_list: list) -> Counter:
    """
        Returns dict with counted birthdays
        input:
            p_list - list of generated birthdays
        output:
            Counter wih counted birthdays
    """
    return Counter(p_list)

def are_same_birthdays_in_list(p_amount: int) -> bool:
    """
        Returns True if there are two or more same birthdays 
        input: 
            p_amount - amount of birthdays to generate
        output:
            bool
    """
    l_counter = count_birthdays(generate_birthdays(p_amount=p_amount))
    return True if max(l_counter.values()) > 1 else False

def test_paradox(p_cases_amt: int, p_people_amt: int) -> dict:
    """
        Returns string <total_cases>/<successful_cases>
        input:
            p_cases_amt - amount of cases
            p_people_amt - amount of people in a room
        output:
            str
    """
    l_result = dict()
    l_success_count = 0
    for i in range(p_cases_amt):
        if are_same_birthdays_in_list(p_amount=p_people_amt):
            l_success_count += 1
    l_result["amount_of_people"] = p_people_amt 
    l_result["amount_of_cases"] = p_cases_amt 
    l_result["amount_of_successful_cases"] = l_success_count
    return l_result

def test_paradox_complex() -> list:
    """
        Runs multiple tests and returns list of result
    """
    l_result = []
    for i in range(5, 101, 5):
        l_result.append(test_paradox(p_cases_amt=100, p_people_amt=i))
    return l_result
