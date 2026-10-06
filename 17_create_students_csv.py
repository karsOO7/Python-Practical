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
