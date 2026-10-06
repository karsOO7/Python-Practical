# ============================================================================
# 01_positive_negative_zero.py
# ============================================================================

# Program to check whether a number is positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# ============================================================================
# 02_multiplication_table.py
# ============================================================================

# Program to print the multiplication table of a number using a for loop
num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ============================================================================
# 03_even_numbers_1_to_50.py
# ============================================================================

# Program to print all even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i, end=" ")


# ============================================================================
# 04_factorial_using_loop.py
# ============================================================================

# Program to find the factorial of a number using a loop
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")


# ============================================================================
# 05_list_operations.py
# ============================================================================

# Program to demonstrate common list operations
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After append(60):", numbers)

numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

numbers.remove(40)
print("After remove(40):", numbers)

popped = numbers.pop()
print(f"Popped value: {popped}, List now: {numbers}")

numbers.sort(reverse=True)
print("Sorted (descending):", numbers)


# ============================================================================
# 06_list_sum_max.py
# ============================================================================

# Program to display the sum and maximum of a list
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Sum of list:", sum(numbers))
print("Maximum value:", max(numbers))


# ============================================================================
# 07_tuple_operations.py
# ============================================================================

# Program to demonstrate tuple indexing, slicing, iteration, and unpacking
coordinates = (10.5, 20.3, 30.7, 40.1)

print("Tuple:", coordinates)
print("Element at index 2:", coordinates[2])
print("Slice [1:3]:", coordinates[1:3])

print("Iterating over the tuple:")
for value in coordinates:
    print(value, end=" ")
print()

x, y, z, w = coordinates
print(f"Unpacked values: x={x}, y={y}, z={z}, w={w}")


# ============================================================================
# 08_numpy_arrays.py
# ============================================================================

# Program to create arrays using zeros(), ones(), arange(), and linspace()
import numpy as np

print("Zeros:")
print(np.zeros((2, 3)))

print("Ones:")
print(np.ones((3, 2)))

print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))


# ============================================================================
# 09_dictionary_add_update_delete.py
# ============================================================================

# Program to demonstrate adding, updating, and deleting dictionary keys
student = {
    "name": "Aditi Sharma",
    "roll_no": 21,
    "branch": "Computer Science",
    "marks": 88
}

print("Original dictionary:", student)

student["attendance"] = "92%"  # add a new key
student["marks"] = 91            # update an existing key
print("After adding/updating:", student)

del student["branch"]             # delete a key
print("After deleting 'branch':", student)


# ============================================================================
# 10_numpy_marks_indexing.py
# ============================================================================

# Program for indexing, slicing, reversing, and boolean indexing
import numpy as np

marks = np.array([56, 78, 92, 45, 88, 67, 34, 99])

print("Marks:", marks)
print("Element at index 2:", marks[2])
print("Slice [2:6]:", marks[2:6])
print("Reversed:", marks[::-1])
print("Marks >= 70:", marks[marks >= 70])


# ============================================================================
# 11_dictionary_keys_values_items.py
# ============================================================================

# Program to print all keys, values, and items of a dictionary
student = {
    "name": "Aditi Sharma",
    "roll_no": 21,
    "branch": "Computer Science",
    "marks": 88
}

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:")
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================================
# 12_args_sum.py
# ============================================================================

# Function using *args to calculate the sum of any number of values
def total_sum(*args):
    return sum(args)

print(total_sum(10, 20, 30))
print(total_sum(5, 15))
print(total_sum(1, 2, 3, 4, 5))


# ============================================================================
# 13_recursive_factorial.py
# ============================================================================

# Recursive function to calculate factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 6
print(f"Factorial of {num} is {factorial(num)}")


# ============================================================================
# 14_recursive_fibonacci.py
# ============================================================================

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


# ============================================================================
# 15_histogram_exam_marks.py
# ============================================================================

# Program to plot a histogram of exam marks
import matplotlib.pyplot as plt

marks = [35, 42, 48, 52, 55, 58, 60, 62, 64, 65,
         67, 68, 70, 72, 74, 75, 78, 82, 85, 91]

plt.hist(marks, bins=5, color="orange", edgecolor="black")
plt.title("Distribution of Exam Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# ============================================================================
# 16_exception_handling_division.py
# ============================================================================

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


# ============================================================================
# 17_create_students_csv.py
# ============================================================================

# Program to create a DataFrame and save it as a CSV file
import pandas as pd

data = {
    "Name": ["Aarav", "Priya", "Rohan", "Sneha", "Kabir"],
    "Age": [20, 21, 19, 22, 20],
    "Branch": ["CSE", "ECE", "CSE", "IT", "CSE"],
    "Marks": [78, 85, 90, 66, 74]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("students.csv", index=False)
print("Saved to students.csv")


# ============================================================================
# 18_load_inspect_students_csv.py
# ============================================================================

# Program to load a CSV file and inspect it
import pandas as pd

df = pd.read_csv("students.csv")

print("Head:")
print(df.head())
print("Shape:", df.shape)
print("Info:")
df.info()
print("Describe:")
print(df.describe())


# ============================================================================
# 19_student_grade_column.py
# ============================================================================

# Program to add a Grade column based on Marks
import pandas as pd

data = {
    "Name": ["Aarav", "Priya", "Rohan", "Sneha", "Kabir"],
    "Age": [20, 21, 19, 22, 20],
    "Branch": ["CSE", "ECE", "CSE", "IT", "CSE"],
    "Marks": [78, 85, 90, 66, 74]
}

df = pd.DataFrame(data)

grades = []
for m in df["Marks"]:
    if m >= 80:
        grades.append("A")
    elif m >= 70:
        grades.append("B")
    else:
        grades.append("C")

df["Grade"] = grades
print(df)


# ============================================================================
# 20_sales_filter_revenue.py
# ============================================================================

# Program to filter rows where Revenue is greater than 100000
import pandas as pd

data = {
    "Region": ["North", "South", "North", "East", "South", "East", "North", "South"],
    "Product": ["Laptop", "Laptop", "Mouse", "Laptop", "Mouse", "Mouse", "Mouse", "Laptop"],
    "Quantity": [5, 8, 20, 3, 15, 10, 12, 6],
    "Revenue": [250000, 400000, 10000, 150000, 7500, 5000, 6000, 300000]
}

df = pd.DataFrame(data)
high_revenue = df[df["Revenue"] > 100000]

print("Rows with Revenue > 100000:")
print(high_revenue)


# ============================================================================
# 21_sales_filter_south_quantity.py
# ============================================================================

# Program to filter rows where Region is South and Quantity is 6 or more
import pandas as pd

data = {
    "Region": ["North", "South", "North", "East", "South", "East", "North", "South"],
    "Product": ["Laptop", "Laptop", "Mouse", "Laptop", "Mouse", "Mouse", "Mouse", "Laptop"],
    "Quantity": [5, 8, 20, 3, 15, 10, 12, 6],
    "Revenue": [250000, 400000, 10000, 150000, 7500, 5000, 6000, 300000]
}

df = pd.DataFrame(data)
result = df[(df["Region"] == "South") & (df["Quantity"] >= 6)]

print("South region with Quantity >= 6:")
print(result)


# ============================================================================
# 22_sales_2024_2025_line.py
# ============================================================================

# Program to compare sales of two years on the same axes
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2024 = [200, 220, 210, 240, 260, 250]
sales_2025 = [230, 245, 255, 270, 300, 310]

plt.plot(months, sales_2024, marker="o", label="2024")
plt.plot(months, sales_2025, marker="o", label="2025")
plt.title("Sales: 2024 vs 2025")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================================
# 23_monthly_sales_line.py
# ============================================================================

# Program to plot a line chart of monthly sales
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [220, 245, 210, 260, 300, 280, 310, 295, 330, 350, 370, 400]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True)
plt.show()


# ============================================================================
# 24_revenue_by_product_bar.py
# ============================================================================

# Program to plot a bar chart of revenue by product
import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
revenue = [450000, 60000, 85000, 220000, 95000]

plt.bar(products, revenue, color="teal")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.show()


