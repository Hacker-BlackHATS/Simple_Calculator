from art import simple_calculator_logo as logo
from Other_functions import clear


def calculate(first_no, operator, second_no):
    """
    Enter First and Second number and operator.
    """
    if operator == "+":
        return first_no + second_no
    if operator == "-":
        return first_no - second_no
    if operator == "*":
        return first_no * second_no
    if operator == "/":
        return first_no / second_no


def main():
    print(logo)
    f_no = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    iscontinue = "y"
    while iscontinue == "y":
        operator = input("Pick an operation: ")
        s_no = float(input("What's the next number?: "))
        cal_no = calculate(f_no, operator, s_no)
        print(f"{f_no} {operator} {s_no} = {cal_no}")
        iscontinue = input(f"Type 'y' to continue calculating with {cal_no}, or type 'n' to start a new calculation: ").lower()
        f_no = cal_no
    if iscontinue == "n":
        clear()
        main()


main()

# Another way
"""
from Other_functions import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

"""
