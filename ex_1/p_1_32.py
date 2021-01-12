def simple_calculator():
    """
        Each input is done on separate line 
        Only two numbers and one arithmetical expression between is supported   
        To calculate result - input an equation sign
    """
    v_input = []

    while True: 
        v_input.append(input().replace(" ", ""))
        process_input(io_input=v_input)

def process_input(io_input: list):
    """
        Runs checks and prints appropriate message for user 
        Tries to evaluate the expression if possible 
    """

    if len(io_input) > 0:
        last_element = io_input[-1]

    if len(io_input) == 1:
        if last_element == "":
            reset_input(io_input=io_input)
            print("Enter a number:")
        else:
            try:
                float(last_element)
            except ValueError:
                reset_input(io_input=io_input)
                print("User input must be a number!")

    elif len(io_input) == 2:
        if len(last_element) > 0:
            if last_element not in "+-*/" or len(last_element) > 1:
                reset_input(io_input=io_input)
                print("User input must be an operator!")
        else:
            reset_input(io_input=io_input)
            print("Enter an operator. Supported operators are ( + | - | * | / ):")

    elif len(io_input) == 3:
        if last_element == "":
            reset_input(io_input=io_input)
            print("Enter a number:")
        else:
            try:
                if io_input[1] == "/" and float(last_element) == 0:
                    reset_input(io_input=io_input)
                    print("Division by zero!")
            except ValueError:
                reset_input(io_input=io_input)
                print("User input must be a number!")

    elif len(io_input) == 4:
        if len(last_element) > 0 and last_element != "=":
            reset_input(io_input=io_input)
            print("User input must be an equation sign (=)!")
        elif len(last_element) == 0:
            reset_input(io_input=io_input)
            print("Enter an equation sign to calculate the expression:")
        else:
            v_first_number = io_input[0]
            v_operator = io_input[1]
            v_second_number = io_input[2]
            v_result = calculate_expression(
                i_first_number=float(v_first_number),
                i_second_number=float(v_second_number),
                i_operator=v_operator
            )
            print("Result is: " + str(v_result))
            clear_input(io_input=io_input)

    else:
        raise Exception("Something unknown occured!")

def calculate_expression(i_first_number: float, i_second_number: float, i_operator: str) -> float:
    if i_operator == "+":
        return i_first_number + i_second_number 
    elif i_operator == "-":
        return i_first_number - i_second_number 
    elif i_operator == "*":
        return i_first_number * i_second_number
    elif i_operator == "/":
        return i_first_number / i_second_number

def reset_input(io_input: list):
    """
    Deletes last element of a list 
    """
    del io_input[-1]

def clear_input(io_input: list):
    """
    Returns empty list (out parameter)
    """
    while len(io_input) > 0:
        del io_input[-1]

