while True:
    op = input("Enter operator (+, -, *, /) or type 'exit' to quit: ").strip()

    if op.lower() == 'exit':
        print(" Calculator exited. Goodbye!")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print(" Error: Division by zero.")
        else:
            print(" Invalid operator.")

    except ValueError:
        print("Please enter valid numbers.")
