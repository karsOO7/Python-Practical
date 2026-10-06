# Program to plot a histogram of exam marks
import matplotlib.pyplot as plt

marks = [35, 42, 48, 52, 55, 58, 60, 62, 64, 65,
         67, 68, 70, 72, 74, 75, 78, 82, 85, 91]

plt.hist(marks, bins=5, color="orange", edgecolor="black")
plt.title("Distribution of Exam Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
