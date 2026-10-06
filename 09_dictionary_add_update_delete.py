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
