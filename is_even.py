def is_even(x):
    """Function to see if x is even"""
    return x % 2 == 0

assert is_even.__doc__ is not None 
assert is_even(2) is True
assert is_even(1) is False