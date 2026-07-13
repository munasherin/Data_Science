import numpy as np


r1 = int(input("Enter rows for matrix A: "))
c1 = int(input("Enter columns for matrix A: "))
print(f"Enter {r1}  rows(numbers separated by space):")
A = np.array([[float(x) for x in input(f"Row {i+1}: ").split()] for i in range(r1)])


r2 = int(input("\nEnter rows for matrix B: "))
c2 = int(input("Enter columns for matrix B: "))
print(f"Enter {r2}  rows(numbers separated by space): ")
B = np.array([[float(x) for x in input(f"Row {i+1}: ").split()] for i in range(r2)])

print(f"\nMatrix A:\n{A}\n")
print(f"Matrix B:\n{B}\n")

if A.shape == B.shape:
    print(f"Addition (A + B):\n{A + B}\n")
else:
    print(f"Addition not possible (Dimensions must match).\n")

if c1 == r2:
    print(f"Multiplication (A @ B):\n{A @ B}")
else:
    print(f"Multiplication not possible (Columns of A must equal Rows of B).")