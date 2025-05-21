# -----------------------------
# VECTORS
# -----------------------------

# Define two 2D vectors
v1 = [1, 2]
v2 = [3, 4]

# Vector Addition (element-wise)
vector_add = [v1[i] + v2[i] for i in range(len(v1))]
print("Vector Addition:", vector_add)

# Scalar Multiplication
scalar = 3
scaled_vector = [scalar * x for x in v1]
print("Scalar Multiplication:", scaled_vector)

# -----------------------------
# MATRICES
# -----------------------------

# Define two 2x2 matrices
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]

# Matrix Addition (element-wise)
matrix_add = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]
print("Matrix Addition:")
for row in matrix_add:
    print(row)

# Matrix Multiplication
# A: m x n, B: n x p
result = [
    [sum(A[i][k] * B[k][j] for k in range(len(B)))
     for j in range(len(B[0]))]
    for i in range(len(A))
]
print("Matrix Multiplication:")
for row in result:
    print(row)

# -----------------------------
# DOT PRODUCT
# -----------------------------

# Define two 3D vectors
a = [1, 2, 3]
b = [4, 5, 6]

# Dot product: sum of element-wise products
dot_product = sum(a[i] * b[i] for i in range(len(a)))
print("Dot Product:", dot_product)

# -----------------------------
# GEOMETRIC INTERPRETATION (OPTIONAL)
# -----------------------------

import math

# Function to calculate magnitude of a vector
def magnitude(vec):
    return math.sqrt(sum(x**2 for x in vec))

# Angle between vectors using dot product
cos_theta = dot_product / (magnitude(a) * magnitude(b))
theta_radians = math.acos(cos_theta)
theta_degrees = math.degrees(theta_radians)
print("Angle between vectors (degrees):", round(theta_degrees, 2))

# -----------------------------
# APPLICATION DEMO: Cosine Similarity
# -----------------------------

cosine_similarity = dot_product / (magnitude(a) * magnitude(b))
print("Cosine Similarity:", round(cosine_similarity, 4))
