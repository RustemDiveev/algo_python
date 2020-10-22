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

def reverse_output():
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

reverse_output()