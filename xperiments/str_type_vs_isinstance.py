from typing import Sequence 
from random import randint
from time import time 

"""
Check what's faster for type checking
"""

def get_random_element() -> Sequence:
    """
        Initiates and returns random element
        1 - list
        2 - tuple 
        3 - set
        4 - frozenset
        5 - dict 
    """

    v_int = randint(1, 5)
    if v_int == 1:
        return list()
    elif v_int == 2:
        return tuple()
    elif v_int == 3:
        return set()
    elif v_int == 4:
        return frozenset()
    elif v_int == 5:
        return dict()

def get_element_type_by_type(elem: Sequence) -> str:
    """
        Returns type of input element with using of built-in type function
    """
    datatype = str(type(elem))

    if datatype == "<class 'list'>":
        return "list"
    elif datatype == "<class 'tuple'>":
        return "tuple"
    elif datatype == "<class 'set'>":
        return "set"
    elif datatype == "<class 'dict'>":
        return "dict"
    elif datatype == "<class 'frozenset'>":
        return "frozenset"

def get_element_type_by_isinstance(elem: Sequence) -> str:
    """
        Returns type of input element with using of built-in isinstance function
    """

    if isinstance(elem, list):
        return "list"
    elif isinstance(elem, tuple):
        return "tuple"
    elif isinstance(elem, set):
        return "set"
    elif isinstance(elem, dict):
        return "dict"
    elif isinstance(elem, frozenset):
        return "frozenset"

def test_performance(elem_amt):
    v_list = []

    for i in range(elem_amt):
        v_list.append(get_random_element())

    start_time = time()
    for i in v_list:
        a = get_element_type_by_type(i)
    end_time = time()
    print("Time for type is")
    print(end_time - start_time)

    start_time = time()
    for i in v_list:
        a = get_element_type_by_isinstance(i)
    end_time = time()
    print("Time for isinstance is")
    print(end_time - start_time)

test_performance(1000000)

"""
Time for type is
0.8175802230834961
Time for isinstance is
0.31938838958740234

Summary: use isinstance - it'is few times faster
"""