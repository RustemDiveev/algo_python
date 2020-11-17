def input_int() -> int:
    """
        Get int from input
    """
    while True:
        try:
            v_result = int(input())
        except ValueError:
            print("Couldn't cast to integer, try again")
            continue 
        else:
            break

    return v_result

def get_three_input_ints() -> tuple:
    """
        Return tuple with three ints from input
    """
    v_a = input_int()
    v_b = input_int()
    v_c = input_int()
    return (v_a, v_b, v_c)

# WTF? Test doesn't run with input param
def check_correct_arithmetic_formula(i_tuple: tuple) -> bool:
    """
        Takes an input tuple with 3 integers 
        and determines if they can be used in a correct formula in a given order:
        1) a + b = c
        2) a = b - c
        3) a * b = c 
        Returns true if can be used, false otherwise
    """
    a, b, c = i_tuple
    o_result = (a + b == c) | (a == b - c) | (a * b == c)
    return o_result 
