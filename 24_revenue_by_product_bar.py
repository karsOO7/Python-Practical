# Program to plot a bar chart of revenue by product
import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
revenue = [450000, 60000, 85000, 220000, 95000]

plt.bar(products, revenue, color="teal")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.show()
