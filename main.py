
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

cal_operators["+"] = add
cal_operators["-"] = subtract
cal_operators["*"] = multiply
cal_operators["/"] = divide

# print(cal_operators["*"](4, 8))

# ------

# add logo from art.py
# display the logo

# ask user input for first number
first_number = input("What's the first number?: ")
# display the operator use can choose from
print("+\n-\n*\n/\n")
# ask user input for the operator
chosen_operator = input("Pick an operation: ")
# ask user input for second number
second_number = input("What's the second number?: ")
# program work out result based on chosen operator
cal_result = cal_operators["{chosen_operator}"]({first_number}, {second_number})
# display the result
print(cal_result)
# ask use continue with current result
use_current_result = input("Type 'y' to continue calculating with {cal_result}, or type 'n' to start a new calculation: ")
# if yes: 
# 1. use current result as fist number
# 2. go back to user input for operator step
# if no:
# 1. clear the screen
# 2. go back to the start point

# if use_current_result == "y":
    
# how to go back to specific step???