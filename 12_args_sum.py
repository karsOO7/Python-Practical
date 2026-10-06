# Function using *args to calculate the sum of any number of values
def total_sum(*args):
    return sum(args)

print(total_sum(10, 20, 30))
print(total_sum(5, 15))
print(total_sum(1, 2, 3, 4, 5))
