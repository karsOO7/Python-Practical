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
