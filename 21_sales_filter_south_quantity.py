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
