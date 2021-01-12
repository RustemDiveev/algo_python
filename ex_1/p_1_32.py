# TODO
# 1. function for reseting last input 
# 2. function for clearing input 
# 3. get last element at beginning 
# 4. getters for certain elements of input 
# 5. fcking unit tests

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
        # Debug
        print("After processing: " + str(v_input))

def process_input(io_input: list):
    """
        Runs checks and prints appropriate message for user 
        Tries to evaluate the expression if possible 
    """
    print("Before processing: " + str(io_input))

    if len(io_input) == 1:
        if io_input[-1] == "":
            del io_input[-1]
            print("Enter a number:")
        else:
            try:
                float(io_input[-1])
            except ValueError:
                del io_input[-1]
                print("User input must be a number!")

    elif len(io_input) == 2:
        if len(io_input[-1]) > 0:
            if io_input[-1] not in "+-*/" or len(io_input[-1]) > 1:
                del io_input[-1]
                print("User input must be an operator!")
        else:
            del io_input[-1]
            print("Enter an operator. Supported operators are ( + | - | * | / ):")

    elif len(io_input) == 3:
        if io_input[-1] == "":
            del io_input[-1]
            print("Enter a number:")
        else:
            try:
                if io_input[1] == "/" and float(io_input[-1]) == 0:
                    del io_input[-1]
                    print("Division by zero!")
            except ValueError:
                del io_input[-1]
                print("User input must be a number!")

    elif len(io_input) == 4:
        if len(io_input[-1]) > 0 and io_input[-1] != "=":
            del io_input[-1]
            print("User input must be an equation sign (=)!")
        elif len(io_input[-1]) == 0:
            del io_input[-1]
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
            while len(io_input) > 0:
                del io_input[-1]

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

simple_calculator()
