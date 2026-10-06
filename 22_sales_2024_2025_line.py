# Program to compare sales of two years on the same axes
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2024 = [200, 220, 210, 240, 260, 250]
sales_2025 = [230, 245, 255, 270, 300, 310]

plt.plot(months, sales_2024, marker="o", label="2024")
plt.plot(months, sales_2025, marker="o", label="2025")
plt.title("Sales: 2024 vs 2025")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.show()
