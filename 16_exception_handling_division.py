# Program to divide two numbers, handling ZeroDivisionError and ValueError
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integer values.")
else:
    print(f"Result: {num1} / {num2} = {result}")
finally:
    print("Division operation attempted. Program continues normally.")
