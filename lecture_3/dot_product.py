import numpy as np

# Define two vectors
v1 = np.array([1, 30])
v2 = np.array([3, 3])

# Element-wise multiplication
multi_of_v1v2 = v1 * v2
print("Element-wise Multiplication:", multi_of_v1v2)

# Dot product
dot = np.dot(v1, v2)
print("Dot Product:", dot)
