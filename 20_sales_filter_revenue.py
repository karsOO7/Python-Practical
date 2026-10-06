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
