def input_int() -> int:
    """
        Get int from input
    """
    while True:
        try:
            l_result = int(input())
        except ValueError:
            print("Couldn't cast to integer, try again")
            continue 
        else:
            break
    return l_result

def get_three_input_ints() -> tuple:
    """
        Return tuple with three ints from input
        output:
            tuple
    """
    l_a = input_int()
    l_b = input_int()
    l_c = input_int()
    return (l_a, l_b, l_c)

# WTF? Test doesn't run with input param
def check_correct_arithmetic_formula(p_tuple: tuple) -> bool:
    """
        Takes an input tuple with 3 integers 
        and determines if they can be used in a correct formula in a given order:
        1) a + b = c
        2) a = b - c
        3) a * b = c 
        Returns true if can be used, false otherwise
        input:
            p_tuple - input tuple with 3 integers 
        output:
            bool
    """
    a, b, c = p_tuple
    l_result = (a + b == c) | (a == b - c) | (a * b == c)
    return l_result 
