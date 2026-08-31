import matplotlib.pyplot as plt
roll_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks = [22,87,5,43,56,73,55,54,11,20,61,5,79,31,27]
plt.figure(figsize=(9, 5))
plt.scatter(roll_numbers, marks, color='crimson', s=60, edgecolors='black',label='Students')
plt.title("Student Marks vs Roll Number")
plt.xlabel("Roll Number")
plt.ylabel("Marks Obtained")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
