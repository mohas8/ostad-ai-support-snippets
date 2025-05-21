import numpy as np


# Define two vectors
vector_p = np.array([4, 7, 8])
vector_q = np.array([7887, 454, 10])

# Check types
print("Type of vector_p:", type(vector_p))
print("Type of vector_q:", type(vector_q))

# Element-wise addition
sum_vector = vector_p + vector_q
print("Sum:", sum_vector)

# Element-wise multiplication
product_vector = vector_p * vector_q
print("Product (element-wise):", product_vector)
