# Program for indexing, slicing, reversing, and boolean indexing
import numpy as np

marks = np.array([56, 78, 92, 45, 88, 67, 34, 99])

print("Marks:", marks)
print("Element at index 2:", marks[2])
print("Slice [2:6]:", marks[2:6])
print("Reversed:", marks[::-1])
print("Marks >= 70:", marks[marks >= 70])
