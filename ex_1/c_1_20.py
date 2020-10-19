from random import randint, shuffle
from collections import defaultdict

# TODO: Test is shuffle(data) and randint_version_of_shuffle(data) shuffles elements with same probability

def randint_version_of_shuffle(i_list: list) -> list:
    """
        Implementation of shuffle function with usage 
        of random.randint function 
    """

    """
        My version of algorithm (17.10.2020) - maybe there is more effective solution
        1. Select randomly one of the elements 
        2. This element will be first 
        3. Push that element to final list 
        4. Delete element from original list 
        5. Move to step 1, until list is empty
    """

    v_list = i_list.copy()
    v_final_list = []

    while len(v_list) > 0:
        v_selected_elem_idx = randint(0, len(v_list) - 1)
        v_elem = v_list.pop(v_selected_elem_idx)
        v_final_list.append(v_elem)

    return v_final_list


def get_shuffle_probability(i_list: list, i_observation_num: int) -> defaultdict:

    v_dict = defaultdict(int)

    for i in range(i_observation_num):
        v_list = i_list.copy()
        shuffle(v_list)
        v_dict[str(v_list)] += 1

    return v_dict


def get_randint_probability(i_list: list, i_observation_num: int) -> defaultdict:

    v_dict = defaultdict(int)

    for i in range(i_observation_num):
        v_list = randint_version_of_shuffle(i_list)
        v_dict[str(v_list)] += 1

    return v_dict

#print(test_shuffle_probability([1,2,3], 1000000))
#print(test_randint_probability([1,2,3], 1000000))

