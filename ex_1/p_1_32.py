from decimal import Decimal, InvalidOperation

def simple_calculator():
    """
        Simple calculator
        Each input is done on separate line 
        Supported actions: +, -, *, /
    """
    v_operation_list = []

    while True:
        v_str = str(input())
        process_input(io_operation_list=v_operation_list, i_input_str=v_str) 
        print(v_operation_list)

def process_input(io_operation_list: list, i_input_str: str):
    """
        Check input str and add to io_operation_list 
    """
    io_operation_list.append(i_input_str)
    if check_operations(io_operation_list=io_operation_list):
        calculate_result(io_operation_list=io_operation_list) 
    else:
        del io_operation_list[-1]

def check_operations(io_operation_list: list) -> bool:
    """
        Returns True if all checks passed 
        Returns False if otherwise
    """
    if check_decimal(io_operation_list=io_operation_list) and \
        check_operator(io_operation_list=io_operation_list) and \
        check_equity(io_operation_list=io_operation_list) and \
        check_zero(io_operation_list=io_operation_list) and \
        check_length(io_operation_list=io_operation_list):
        return True
    else:
        return False

def check_decimal(io_operation_list: list) -> bool:
    """
        Checks that first and third elements 
        are convertable to decimal 
    """
    try:
        Decimal(io_operation_list[0])
    except IndexError:
        pass
    except InvalidOperation:
        print("First argument must be a number!")
        return False 
    
    try:
        Decimal(io_operation_list[2])
    except IndexError:
        pass 
    except InvalidOperation:
        print("Second argument must be a number!")
        return False 
    
    return True

def check_operator(io_operation_list: list) -> bool:
    """
        2nd element must be one of those: +-*/
    """
    try:
        v_operator = io_operation_list[1]
    except IndexError:
        return True 
    
    if len(v_operator) == 1 and v_operator in "+-*/":
        return True
    else:
        print("Specified operation must be one of those: + | - | * | / |")
        return False

def check_equity(io_operation_list: list) -> bool:
    """
        4th element must be an equation sign
    """
    try:
        v_equation = io_operation_list[3]
    except IndexError:
        return True 

    if v_equation == "=":
        return True
    else:
        print("Equation sign required!")
        return False 

def check_zero(io_operation_list: list) -> bool:
    """
        If division then no zero allowed for second argument
    """
    try:
        v_operation = io_operation_list[1]
        v_second_argument = io_operation_list[2]
    except IndexError:
        return True 
    
    if v_operation == "/" and int(v_second_argument) == 0:
        print("Second division mustn't be zero on division!")
        return False
    else:
        return True 

def check_length(io_operation_list: list) -> bool:
    """
        Checks that operation list length doesn't exceed 5 elements
    """
    return True if len(io_operation_list) <= 5 else False

def calculate_result(io_operation_list: list):
    """
        Calculates and prints result and deletes all elements from list
    """
    if len(io_operation_list) == 4:
        v_first_argument = io_operation_list[0]
        v_second_argument = io_operation_list[2]
        v_operation = io_operation_list[1]

        if v_operation == "+":
            v_result = Decimal(v_first_argument) + Decimal(v_second_argument)
        elif v_operation == "-":
            v_result = Decimal(v_first_argument) - Decimal(v_second_argument)
        elif v_operation == "*":
            v_result = Decimal(v_first_argument) * Decimal(v_second_argument)
        elif v_operation == "/":
            v_result = Decimal(v_first_argument) / Decimal(v_second_argument)

        print(str(v_result))
        io_operation_list = []
     
simple_calculator()