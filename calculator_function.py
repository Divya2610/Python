#calculator
from calculator import logo

#Add
def add (n1, n2):
    return n1 + n2 

#Subtraction
def sub (n1, n2):
    return n1 - n2

#Multiply
def mul (n1, n2):
    return n1 * n2

#Divide
def div (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:") == "y":
            num1 = answer
        else:
            should_continue = False
calculator()