# data - is list - list is mutable
# data[i] - is int - int is immutable
# mutable types can be changed 
# holding the same reference to same memory block
# Ex 1.
# data = [1,2], factor = 2
# before function call: id(data) = a, id(data[0]) = b, id(data[1]) = c
# after function call id(data) = a, id(data[0]) = z, id(data[1]) = y
# but data = [2,4]
# Check tests for proofs

def scale(po_data: list, p_factor: int):
    """
        Multiplies all elements in po_data list by p_factor
        input:
            po_data - list of elements
            p_factor - multiplier
        output:
            po_data is an out parameter
    """
    for j in range(len(po_data)):
        po_data[j] *= p_factor

# Also, immutable type won't be changed after function call 
# Basically, this function does nothing
# Ex 2.
# before function call: num = 10, id(num) = a
# after function call: num = 10, id(num) = a
# Check tests for proofs

def multiply_x_2(p_num: int):
    p_num *= 2
