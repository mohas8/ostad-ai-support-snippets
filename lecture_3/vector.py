import numpy as np


# Define a 4-dimensional vector
v = np.array([1, 2, 3, 4])
print("v =", v)
print("Type:", type(v))
print("Shape:", v.shape)

u = np.array([10, 20, 30, 40])
w = v + u
print("u =", u)
print("v + u =", w)

alpha = 3
scaled = alpha * v
print(f"{alpha} * v =", scaled)

# 2×3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("A =\n", A)
print("Shape:", A.shape)   # (rows, columns)

B = np.array([[10, 20, 30],
              [40, 50, 60]])
print("A + B =\n", A + B)


# A is 2×3, v must be length-3
v3 = np.array([1, 0, -1])
result = A.dot(v3)        # or np.matmul(A, v3)
print("A · v3 =", result)  # yields shape (2,)



# C is 3×2 so that A (2×3) × C (3×2) = D (2×2)
C = np.array([[1, 2],
              [3, 4],
              [5, 6]])
D = A.dot(C)
print("C =\n", C)
print("A × C =\n", D)

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
dp = np.dot(u, v)
print("u · v =", dp)   # 1*4 + 2*5 + 3*6 = 32


# Compute norms
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
cos_theta = dp / (norm_u * norm_v)
theta = np.arccos(cos_theta)   # in radians

print("‖u‖ =", norm_u)
print("‖v‖ =", norm_v)
print("cosθ =", cos_theta)
print("θ (degrees) =", np.degrees(theta))

