def simple_calculator():
    """
        Each input is done on separate line 
        Only two numbers and one arithmetical expression between is supported   
        To calculate result - input an equation sign
    """
    l_input = []
    while True: 
        l_input.append(input().replace(" ", ""))
        process_input(po_input=l_input)

def process_input(po_input: list):
    """
        Runs checks and prints appropriate message for user 
        Tries to evaluate the expression if possible 
        input:
            po_input - input and output list of two numbers and operator
    """
    if len(po_input) > 0:
        l_last_element = po_input[-1]

    if len(po_input) == 1:
        if l_last_element == "":
            reset_input(po_input=po_input)
            print("Enter a number:")
        else:
            try:
                float(l_last_element)
            except ValueError:
                reset_input(po_input=po_input)
                print("User input must be a number!")
    elif len(po_input) == 2:
        if len(l_last_element) > 0:
            if l_last_element not in "+-*/" or len(l_last_element) > 1:
                reset_input(po_input=po_input)
                print("User input must be an operator!")
        else:
            reset_input(po_input=po_input)
            print("Enter an operator. Supported operators are ( + | - | * | / ):")
    elif len(po_input) == 3:
        if l_last_element == "":
            reset_input(po_input=po_input)
            print("Enter a number:")
        else:
            try:
                if po_input[1] == "/" and float(l_last_element) == 0:
                    reset_input(po_input=po_input)
                    print("Division by zero!")
            except ValueError:
                reset_input(po_input=po_input)
                print("User input must be a number!")
    elif len(po_input) == 4:
        if len(l_last_element) > 0 and l_last_element != "=":
            reset_input(po_input=po_input)
            print("User input must be an equation sign (=)!")
        elif len(l_last_element) == 0:
            reset_input(po_input=po_input)
            print("Enter an equation sign to calculate the expression:")
        else:
            l_first_number = po_input[0]
            l_operator = po_input[1]
            l_second_number = po_input[2]
            l_result = calculate_expression(
                p_first_number=float(l_first_number),
                p_second_number=float(l_second_number),
                p_operator=l_operator
            )
            print("Result is: " + str(l_result))
            clear_input(po_input=po_input)
    else:
        raise Exception("Something unknown occured!")

def calculate_expression(p_first_number: float, p_second_number: float, p_operator: str) -> float:
    """
        Calculates expression
        input:
            p_first_number - first number
            p_second_number - second number 
            p_operator - operator 
        output:
            float - result of calculation
    """
    if p_operator == "+":
        return p_first_number + p_second_number 
    elif p_operator == "-":
        return p_first_number - p_second_number 
    elif p_operator == "*":
        return p_first_number * p_second_number
    elif p_operator == "/":
        return p_first_number / p_second_number

def reset_input(po_input: list):
    """
        Deletes last element of a list 
        input:
            po_input - input and output list 
        output:
            po_input
    """
    del po_input[-1]

def clear_input(po_input: list):
    """
        Returns empty list (out parameter)
        input:
            po_input - input and output list
        output:
            po_input
    """
    while len(po_input) > 0:
        del po_input[-1]
