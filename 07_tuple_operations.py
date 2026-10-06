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
