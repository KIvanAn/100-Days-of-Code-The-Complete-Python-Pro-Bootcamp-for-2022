from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n2 == 0:
        different_num = float(input("You can't divide by zero. Choose another number: "))
        return divide(n1, different_num)
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    finish_calculation = False
    num1 = float(input("What's the first number?: "))

    while not finish_calculation:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the second number?: "))

        calculation_func = operations[operation_symbol]
        answer = calculation_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        is_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if is_continue == "y":
            num1 = answer
        else:
            finish_calculation = True
            calculator()


calculator()
