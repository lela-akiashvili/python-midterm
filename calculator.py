def calculator():

    print("Enter two numbers")

    while True:

        # Get valid first number
        while True:
            raw1 = input("Enter the first number: ").strip().replace(",", ".")
            try:
                num1 = float(raw1)
                break
            except ValueError:
                print("Invalid number — please enter a valid numeric value.")

        # Get valid second number
        while True:
            raw2 = input("Enter the second number: ").strip().replace(",", ".")
            try:
                num2 = float(raw2)
                break
            except ValueError:
                print("Invalid number — please enter a valid numeric value.")

        # Get valid operation
        while True:
            operation = input("Choose operation (+, -, *, /): ").strip()
            if operation in ["+", "-", "*", "/"]:
                if operation == "/" and num2 == 0:
                    print("Division by zero is not allowed. Enter a different second number.")
                    # re-ask second number if dividing by zero
                    while True:
                        raw2 = input("Enter the second number: ").strip().replace(",", ".")
                        try:
                            num2 = float(raw2)
                            if num2 == 0:
                                print("Still zero — cannot divide by zero.")
                                continue
                            break
                        except ValueError:
                            print("Invalid number — please enter a valid numeric value.")
                break
            else:
                print("Invalid operation — use only +, -, * or /.")

        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2

        print(f"Result: {result}")

        # Continue?
        again = input("Continue? (y/n): ").strip().lower()
        if again != "y":
            print("Calculator finished.")
            break


if __name__ == "__main__":
    calculator()