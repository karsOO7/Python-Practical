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
