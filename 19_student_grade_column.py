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
