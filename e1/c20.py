from random import randint, shuffle
from collections import defaultdict

def randint_version_of_shuffle(p_list: list) -> list:
    """
        Implementation of shuffle function with usage 
        of random.randint function 
        input:
            p_list - input list with any elements 
        output:
            list - shuffled p_list
    """
    """
        My version of algorithm (17.10.2020) - maybe there is more effective solution
        1. Select randomly one of the elements 
        2. This element will be first 
        3. Push that element to final list 
        4. Delete element from original list 
        5. Move to step 1, until list is empty
    """
    l_list = p_list.copy()
    l_final_list = []
    while len(l_list) > 0:
        l_selected_elem_idx = randint(0, len(l_list) - 1)
        l_elem = l_list.pop(l_selected_elem_idx)
        l_final_list.append(l_elem)
    return l_final_list

def get_shuffle_probability(p_list: list, p_observation_num: int) -> defaultdict:
    """
        Returns default dict with amount of results by shufflng list with usage of built-in function
        input:
            p_list - any list with elements 
            p_observation_num - amount of observations 
        output:
            defaultdict - dictionary with results of hypothesis
    """
    l_dict = defaultdict(int)
    for i in range(p_observation_num):
        l_list = p_list.copy()
        shuffle(l_list)
        l_dict[str(l_list)] += 1
    return l_dict

def get_randint_probability(p_list: list, p_observation_num: int) -> defaultdict:
    """
        Returns default dict with amount of results by shufflng list with usage of implemented function
        input:
            p_list - any list with elements 
            p_observation_num - amount of observations 
        output:
            defaultdict - dictionary with results of hypothesis
    """
    l_dict = defaultdict(int)
    for i in range(p_observation_num):
        l_list = randint_version_of_shuffle(p_list)
        l_dict[str(l_list)] += 1
    return l_dict

#print(test_shuffle_probability([1,2,3], 1000000))
#print(test_randint_probability([1,2,3], 1000000))

