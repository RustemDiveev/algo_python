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
    l_list = []
    try: 
        while True:
            l_line = str(input())
            # Prepends to list
            l_list.insert(0, l_line[::-1])
    except EOFError:
        for line in l_list:
            print(line)

def get_input() -> str:
    """
        Helper - reads and returns input then EOFError raises
        output:
            str - adds new line at the beginning
    """
    l_str = ""
    try:
        while True: 
            l_line = str(input)
            l_str += "\n" + l_line
    except EOFError:
        return l_str

def reverse_str(p_str: str) -> str:
    """
        Helper - reverses string
        input:
            p_str - input string 
        output:
            str - reversed string
    """
    return p_str[::-1]

def reverse_output(p_print_flg: int=1) -> str:
    """
        Reads lines from std until EOFError is raised 
        then outputs lines in reverse order, and returns l_str
        input:
            p_print_flg - flag to print result to stdout
        output:
            str - reversed string
    """
    l_str = get_input()
    l_str = reverse_str(p_str=l_str)
    if p_print_flg == 1:
        print(l_str)
    # For unit tests
    return l_str
