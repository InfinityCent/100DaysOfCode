from typing import Union

print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")


def user_inputs() -> tuple[float, str, float]:
    """

    :return: a tuple with the first number, a desired operator, and the second
             number.
    """
    fn = input("What is the first number? ")
    while not fn.isnumeric():
        fn = input("Please enter a numberic number: ")

    op = input("Pick an operation: +, -, *, / ")
    while op not in ['+', '-', '*', '/']:
        op = input("Please only choose from the following: +, -, *, / ")

    sn = input("What is the second number? ")
    while not sn.isnumeric():
        sn = input("Please enter a numeric number: ")

    return float(fn), op, float(sn)


def user_inputs_trunc() -> tuple[str, float]:
    """

    :return: a tuple with the first number, a desired operator, and the second
             number.
    """
    op = input("Pick an operation: +, -, *, / ")
    while op not in ['+', '-', '*', '/']:
        op = input("Please only choose from the following: +, -, *, / ")

    sn = input("What is the next number? ")
    while not sn.isnumeric():
        sn = input("Please enter a numeric number: ")

    return op, float(sn)


def add(num1: float, num2: float):
    """

    :param num1: first number
    :param num2: second number
    :return: addition of first and second number
    """
    return num1 + num2


def calculate(num1: float, num2: float, op: str) -> Union[float, str]:
    """

    :param num1: first number
    :param num2: second number
    :param op: user's desired operation
    :return: operation applied to first and second number
    """
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

    return 'error'


def run_calculator():
    fn, op, sn = user_inputs()
    cont = 'y'

    while cont in ['y', 'n']:

        output = calculate(fn, sn, op)

        print(f'{fn} {op} {sn} = {output}')
        cont = input(f"Type 'y' to continue calculating with {output}, or type "
                     f"'n' to start a new calculation. Type anything else to "
                     f"quit: ").lower()

        if cont == 'y':
            fn = output
            op, sn = user_inputs_trunc()
        elif cont == 'n':
            fn, op, sn = user_inputs()


run_calculator()
