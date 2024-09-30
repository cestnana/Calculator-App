"""_summary_

Returns:
    _type_: _description_
"""


# add:
def add(n1, n2):
    return n1 + n2


# subtract:
def subtract(n1, n2):
    return n1 - n2


# multiply:
def multiply(n1, n2):
    return n1 * n2


# divide:
def divide(n1, n2):
    return n1 / n2


cal_operators = {}

# This line of code `cal_operators["+"] = add` is assigning the `add` function to the key `"+"` in the
# `cal_operators` dictionary. This means that when you access `cal_operators["+"]`, it will return the
# `add` function, allowing you to use it as a calculator operator for addition.
cal_operators["+"] = add
cal_operators["-"] = subtract
cal_operators["*"] = multiply
cal_operators["/"] = divide

# `print(cal_operators["*"](4, 8))` is using the `cal_operators` dictionary to retrieve the `multiply`
# function and then calling that function with arguments `4` and `8`. This will perform the
# multiplication operation on the numbers `4` and `8` and print the result, which in this case would
# be `32`.
print(cal_operators["*"](4, 8))