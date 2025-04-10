import math_utils

operations = {
    '+': math_utils.add,
    '-': math_utils.sub,
    '*': math_utils.mul,
    '/': math_utils.div,
    '^': math_utils.pow,
    '%': math_utils.mod
}


if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operator = input("Enter an operator (+, -, *, /, ^, %): ")

        # Check if the operator is valid
        if operator in operations:
            result = operations[operator](x, y)
            print(f"The result of {x} {operator} {y} is: {result}")
        else:
            print("Invalid enter")
    except ValueError:
        print("Invalid enter")
