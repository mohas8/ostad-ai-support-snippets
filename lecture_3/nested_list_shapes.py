import numpy as np


# Manually created nested list (not yet a numpy array)
vector_example = [
    [7, 11, 56, 89],
    [8, 9],
    [2, 4],
    [10, 4, 6, 9, 0],
    [1, 2]
]

print("List of Lists:", vector_example)

# Length of outer list
print("Length of outer list:", len(vector_example))

# Lengths of each sub-list
print("Lengths of each sub-list:", [len(sublist) for sublist in vector_example])

arr = np.array(vector_example, dtype=object)
print("Array created from list of lists:", arr)
print("Array shape (using object dtype):", arr.shape)

# # Using np.shape directly
# shape_of_list = np.array(vector_example, dtype=object).shape
# print("Shape using np.shape:", shape_of_list)
#
