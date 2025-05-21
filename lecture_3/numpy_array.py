import numpy as np


arr = np.array(vector_example, dtype=object)
print("Array shape (using object dtype):", arr.shape)

# Using np.shape directly
shape_of_vector_example = np.shape(vector_example)
print("Shape using np.shape():", shape_of_vector_example)
