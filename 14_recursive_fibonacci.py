# Recursive function to print the first n Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of Fibonacci terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i), end=" ")
