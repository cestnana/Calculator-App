# add logo from art.py
from art import logo

# ---------------------
#function declarations:

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
    # return n1 / n2
    # handle divided by zero case
    try:
      return n1 / n2
    except ZeroDivisionError:
      print("Error: Cannot divide by zero.")
      # print("Number cannot divided be zero('0'), please chose another number.")
      return None
      # return 0

# display operators
def display_operators():
  for operator in cal_operators:
    print(operator)

# reset the result
def reset_result(arg):
  # clear the screen
  print("\n" * 20)
  # reset the calculation result
  arg = 0.0
  return arg

# input operator
def input_operator(arg):
    # ask user input for the operator
  arg = input("Pick an operation: ")
  # Handle unavailable operator case:
  while arg not in cal_operators:
    print("Please choose a valid operator.")
    print(f"Your first number is: {first_number}")
    for operator in cal_operators:
      print(operator)
    # ask user input for the operator
    arg = input("Pick an operation: ")
  return arg

# input first number
def input_first_number(arg):
  while True:
    # ask user input for first number
    arg = input("What's the first number?: ")
    # test input is a number or not
    try:
      value = float(arg)
      # if input is a number, return the value
      return arg
    # if input is not a number:
    except ValueError:
      # catch the error and handle it
      print("What you entered is not a number. Please re-enter it.")

def input_second_number(arg):
  while True:
    # ask user input for second number
    arg = input("What's the second number?: ")
    # test input is a number or not
    try:
      value = float(arg)
      # if input is a number, return the value
      return arg
    # if input is not a number:
    except ValueError:
      # catch the error and handle it
      print("What you entered is not a number. Please re-enter it.")

# -------------------------------------------
# Initialize Variables / Lists / Dictionaries

# Initialized cal_operators
cal_operators = {}
# add default operators into dictionary
cal_operators["+"] = add
cal_operators["-"] = subtract
cal_operators["*"] = multiply
cal_operators["/"] = divide

# Initialized chosen_operator
chosen_operator = 0

# Initialized first number
first_number = 0.0

# Initialized second number
second_number = 0.0

# Initialized the calculation result
cal_result = 0.0

# Initialized the continue flag
is_continue_cal = "n"

# set the flag if program run of not
is_program_runs = True

# -------------------------------------
# main logic

while is_program_runs: 
  # *** "No" point when user choose "n"
  if is_continue_cal == "n":
    # reset the calculation result
    reset_result(cal_result)
    # display the logo
    print(logo)
    # handle first number input
    first_number = input_first_number(first_number)
  # *** "Yes" point when user choose "y"
  elif is_continue_cal == "y":
    # if user continued from previous round:
    first_number = cal_result
  # display the operator user can choose from
  # expected output is like: print("+\n-\n*\n/\n")
  display_operators()
  # handle operator input
  chosen_operator = input_operator(chosen_operator)
  # handle second number input
  second_number = input_second_number(second_number)
  
  # Handle "ZeroDivisionError" issue:
  if float(second_number) == 0 or 0.0:
    print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
    # tell the program to stop
    is_continue_cal = "q"
  # if no input issue:
  else:
    # program work out result based on chosen operator
    cal_result = cal_operators[chosen_operator](float(first_number), float(second_number))
    # display the result with display whole calculation
    print(f"{first_number} {chosen_operator} {second_number} = {cal_result}")
    # ask user for: continue/reset/quit
    is_continue_cal = input(f"Type 'y' to continue calculating with {cal_result}, or type 'n' to start a new calculation, otherwise type 'q' to Quit: ")
    # tell program no need to repeat if user want to quit
    if is_continue_cal == "q":
      is_program_runs = False
