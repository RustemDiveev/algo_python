# TODO: Rewrite to test with unittest.mock 
"""
    1. Function which returns input in one str 
    2. Function which returns output in one str
    
    Algo:
    1. Read from input until EOF - return str
    2. Transform str and return result
    3. Print result 
    4. Mock 1 and 3 for testing
"""

# Not suitable for mock unit testing 
# Want to avoid mess with os.system etc
def reverse_output_old():
    """
    Reads lines from std until EOFError is raised 
    then outputs lines in reverse order
    """

    v_list = []

    try: 
        while True:
            v_line = str(input())
            # Prepends to list
            v_list.insert(0, v_line[::-1])
    except EOFError:
        for line in v_list:
            print(line)

def get_input() -> str:
    """
    Helper - reads and returns input then EOFError raises
    """
    v_str = ""

    try:
        while True: 
            v_line = str(input)
            v_str += "\n" + v_line
    except EOFError:
        return v_str

def reverse_str(i_str: str) -> str:
    """
    Helper - reverses string
    """
    return i_str[::-1]

def reverse_output(print_flg:int=1):
    """
    Reads lines from std until EOFError is raised 
    then outputs lines in reverse order, and returns v_str
    """
    v_str = get_input()
    v_str = reverse_str(i_str=v_str)
    if print_flg == 1:
        print(v_str)
    # For unit tests
    return v_str
