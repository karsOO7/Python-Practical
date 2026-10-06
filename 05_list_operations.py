# Program to demonstrate common list operations
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After append(60):", numbers)

numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

numbers.remove(40)
print("After remove(40):", numbers)

popped = numbers.pop()
print(f"Popped value: {popped}, List now: {numbers}")

numbers.sort(reverse=True)
print("Sorted (descending):", numbers)
