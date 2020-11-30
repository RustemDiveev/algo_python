from typing import List

def get_all_possible_strings_using_character_once(i_str: str) -> List[str]:
    """
        Returns all possible combinations of strings consists of letters of one string 
        which used only once
    """
    v_final_list = []

    if not check_unique_symbols_in_string(i_str=i_str):
        raise ValueError("Input string must contain unique characters!")

    if len(i_str) == 0:

        raise ValueError("Input string must contain at least one character")

    elif len(i_str) == 1:

        v_final_list.append(i_str)

    elif len(i_str) == 2:

        first_symbol = i_str[0]
        second_symbol = i_str[1]
        v_final_list.append(first_symbol + second_symbol)
        v_final_list.append(second_symbol + first_symbol)

    else:
        for i in i_str:
            v_less_str = i_str.replace(i, "")
            v_less_list = get_all_possible_strings_using_character_once(i_str=v_less_str)
            v_final_list += [i + string for string in v_less_list]

    return v_final_list

def check_unique_symbols_in_string(i_str: str) -> bool:
    """
        Checks that input string contains unique characters
        Returns True if it is, False otherwise
    """
    if len(list(i_str)) == len(set(i_str)):
        return True
    else:
        return False


def get_all_strings_2(i_str="ab"): 
    first_symbol = i_str[0]
    second_symbol = i_str[1]
    return [first_symbol + second_symbol, second_symbol + first_symbol]

def get_all_strings_3(i_str="abc"):
    v_final_list = []
    for i in i_str:
        v_str = i_str.replace(i, "")
        v_result = get_all_strings_2(i_str=v_str)
        v_list = [i + string for string in v_result]
        v_final_list += v_list 
    return v_final_list

def get_all_strings_4(i_str="abcd"):
    v_final_list = []
    for i in i_str:
        v_str = i_str.replace(i, "")
        v_result = get_all_strings_3(i_str=v_str)
        v_list = [i + string for string in v_result]
        v_final_list += v_list 
    return v_final_list

def get_all_strings(i_str: str):
    v_final_list = []

    if len(i_str) == 1:
        return [i_str]
    if len(i_str) == 2:
        first_symbol = i_str[0]
        second_symbol = i_str[1]
        return [first_symbol + second_symbol, second_symbol + first_symbol]        
    else:
        for i in i_str:
            v_str = i_str.replace(i, "")
            v_result = get_all_strings(i_str=v_str)
            v_final_list += [i + string for string in v_result]
        return v_final_list

#print(get_all_strings_2())
#print(get_all_strings_3())
#print(get_all_strings_4())
#print(get_all_strings(i_str="abcd"))