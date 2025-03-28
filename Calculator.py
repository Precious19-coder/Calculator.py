def calculator():
    """Performs basic arithmetic operations based on user input."""

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operation (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operator. Please use +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
