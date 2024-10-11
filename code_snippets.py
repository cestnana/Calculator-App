# input validation (handle NaN)

# def input_number(arg):
#   user_input = arg
#   while True:
    
#     try:
#       value = float(user_input)
#       print("The value you entered is:", value)
#       break  # Input correctly will exit the loop
#     except ValueError:
#       # catch the error and handle it
#       print("What you entered is not a number. Please re-enter it.")
        
#   return float(user_input)

# ------

# cal_operators = {}

# cal_operators["+"] = add
# cal_operators["-"] = subtract
# cal_operators["*"] = multiply
# cal_operators["/"] = divide

# test print calculation
# print(cal_operators["*"](4, 8))

# ---

    # input first number: 
    
    # while True:
      
    #   # ask user input for first number
    #   first_number = input("What's the first number?: ")
    #   # user_input = input("Please enter a number:")

    #   try:
    #     value = float(first_number)
    #     print("The value you entered is:", value)
    #     break  # Input correctly will exit the loop
    #   except ValueError:
    #     # catch the error and handle it
    #     print("What you entered is not a number. Please re-enter it.")
    
# ---

  # --- handle operator input
    
  # # ask user input for the operator
  # chosen_operator = input("Pick an operation: ")
  # # Handle unavailable operator case:
  # while chosen_operator not in cal_operators:
  #   print("Please choose a valid operator.")
  #   print(f"Your first number is: {first_number}")
  #   for operator in cal_operators:
  #     print(operator)
  #   # ask user input for the operator
  #   chosen_operator = input("Pick an operation: ")
    
  # --- handle operator input
  
# ---

    # if first_number != None:
    #   first_number = cal_result
    # else:
    #   first_number = float(0)
    
    
# ---

  # ask user input for second number
  # second_number = input("What's the second number?: ")
  
  
  # ----- handle second number input
  
  # while True:
  
  #   # ask user input for second number
  #   second_number = input("What's the second number?: ")
  #   # user_input = input("Please enter a number:")

  #   try:
  #     value = float(second_number)
  #     # print("The value you entered is:", value)
  #     break  # Input correctly will exit the loop
  #   except ValueError:
  #     # catch the error and handle it
  #     print("What you entered is not a number. Please re-enter it.")
  
  # # Handle "ZeroDivisionError" issue:
  # if int(second_number) == 0:
  #   # print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
  #   # continue_cal = "y"
  #   print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
  #   # tell the program to stop
  #   continue_cal = "q"
  #   # exit the loop
  #   # break
    
    # ----- handle second number input
    
  
  
    # # Handle "ZeroDivisionError" issue:
  # if float(second_number) == 0 or 0.0:
  #   # print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
  #   # continue_cal = "y"
  #   print(f"Number cannot divided be zero('0'), please choose another number.\nYour first number is: {first_number}")
  #   # tell the program to stop
  #   continue_cal = "q"
  #   # exit the loop
  #   # break
  

  #     # ask user input for the operator
  # chosen_operator = input("Pick an operation: ")
  # # Handle unavailable operator case:
  # while chosen_operator not in cal_operators:
  #   print("Please choose a valid operator.")
  #   print(f"Your first number is: {first_number}")
  #   for operator in cal_operators:
  #     print(operator)
  #   # ask user input for the operator
  #   chosen_operator = input("Pick an operation: ")
  
  
