# Program to find the factorial of a number using a loop
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
