import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Use a list (not a set) so repeated marks are all counted
marks = [22, 45, 67, 89, 34, 56, 23, 12, 45, 67, 78, 67, 45, 34, 89, 100]

bins = list(range(0, 101, 10))

plt.figure(figsize=(9, 5))
counts, _, _ = plt.hist(marks, bins=bins, edgecolor='black', color='skyblue')

plt.title("Distribution of Student Marks")
plt.xlabel("Marks Intervals")
plt.ylabel("Number of Students")
plt.xticks(bins)
plt.yticks(range(0, int(max(counts)) + 2))  # y-axis adapts to the data
plt.grid(axis='y', alpha=0.75)
plt.show()