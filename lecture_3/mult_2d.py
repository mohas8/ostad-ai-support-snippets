import numpy as np


# Define two 2D matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication using np.dot()
result = np.dot(A, B)
print("Matrix Multiplication Result:\n", result)
