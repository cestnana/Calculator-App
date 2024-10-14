# Import logo from art.py
from art import logo

# ---------------------
# Function declarations:

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  """Handles division and checks for division by zero."""
  try:
    return n1 / n2
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    return None

def display_operators():
  """Displays available operators."""
  print("Available operations:")
  print("\n".join(cal_operators))

def get_number(prompt):
  """Prompts the user for a number and validates input."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid input. Please enter a valid number.")

def get_operator():
  """Prompts the user for a valid operator."""
  while True:
    operator = input("Pick an operation: ")
    if operator in cal_operators:
      return operator
    print("Invalid operator. Please choose a valid operation.")

def reset_screen():
  """Clears the screen and resets the result."""
  print("\n" * 20)

# -------------------------------------------
# Initialize Operators Dictionary
cal_operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# -------------------------------------
# Main logic
def calculator():
  """Main calculator function to control program flow."""
  while True:
    reset_screen()
    print(logo)
    first_number = get_number("What's the first number?: ")

    while True:
      display_operators()
      operator = get_operator()
      second_number = get_number("What's the second number?: ")

      # Handle division by zero error early
      if operator == "/" and second_number == 0:
        print("Error: Cannot divide by zero. Please enter a different number.")
        continue

      # Perform calculation
      result = cal_operators[operator](first_number, second_number)
      print(f"{first_number} {operator} {second_number} = {result}")

      # Ask user if they want to continue
      choice = input(f"Type 'y' to continue with {result}, 'n' to start a new calculation, or 'q' to quit: ").lower()
      if choice == 'y':
        first_number = result  # Continue with previous result
      elif choice == 'n':
        break  # Start new calculation
      elif choice == 'q':
        print("Goodbye!")
        return  # Exit program

# Run the calculator
calculator()