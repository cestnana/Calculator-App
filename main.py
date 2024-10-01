# add logo from art.py
import art

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

cal_operators = {}

cal_operators["+"] = add
cal_operators["-"] = subtract
cal_operators["*"] = multiply
cal_operators["/"] = divide

# test print calculation
# print(cal_operators["*"](4, 8))

# ------

def reset_result(arg):
  # clear the screen
  print("\n" * 20)
  # reset the calculation result
  arg = 0.0
  return arg

# Initialized the calculation result
cal_result = 0.0

# Initialized the continue flag
continue_cal = "n"

# set the flag if program run of not
program_runs = True

while program_runs: 
  # "No" point when user choose "n"
  if continue_cal == "n":
  # # display the logo
    # print(art.logo)
  # # reset the calculation result
  # cal_result = 0.0 -> write a function to deal with this
    reset_result(cal_result)
    # display the logo
    print(art.logo)
    # ask user input for first number
    first_number = float(input("What's the first number?: "))
  # "Yes" point when user choose "y"
  elif continue_cal == "y":
    first_number = cal_result
  # display the operator use can choose from
  # print("+\n-\n*\n/\n")
  for operator in cal_operators:
    print(operator)
  # ask user input for the operator
  chosen_operator = input("Pick an operation: ")
  # Handle unavailable operator case:
  while chosen_operator not in cal_operators:
    print("Please a choose valid operator.")
    print(f"Your first number is: {first_number}")
    for operator in cal_operators:
      print(operator)
    # ask user input for the operator
    chosen_operator = input("Pick an operation: ")
  # ask user input for second number
  second_number = float(input("What's the second number?: "))
  # Handle "ZeroDivisionError" issue:
  if second_number == 0:
    print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
    continue_cal = "y"
  else:
    # program work out result based on chosen operator
    cal_result = cal_operators[chosen_operator](first_number, second_number)
    # display the result with display whole calculation
    print(f"{first_number} {chosen_operator} {second_number} = {cal_result}")
    # ask user for: continue/reset/quit
    continue_cal = input(f"Type 'y' to continue calculating with {cal_result}, or type 'n' to start a new calculation, otherwise type 'q' to Quit: ")
    # tell program no need to repeat if user want to quit
    if continue_cal == "q":
      program_runs = False
    
  # if yes: 
  # 1. use current result as fist number
  # 2. go back to user input for operator step
  # if no:
  # 1. clear the screen
  # 2. go back to the start point

  # if use_current_result == "y":

  # how to go back to specific step???
  # -> goto is not recommended and even not built-in feature
  # -> implementing with while loop and if/elif conditional checking