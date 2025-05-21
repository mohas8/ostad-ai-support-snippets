import numpy as np

# a1 = np.arange(1, 13)
#
# B = np.array([[10, 20, 30],
#               [40, 50, 60]])
#
#
# # print("A1:", a1)
#
#
# # print("A1:", a1.reshape(3, 4))
# #
#
# # print("A1:", a1.reshape(-1, 4))
# print(B.reshape(-1, 3))

a = np.array([1, 2, 3])
b = np.array([4, 5])
# a + b  # ValueError

b_padded = np.pad(b, (0, len(a) - len(b)), constant_values=0)
print(a + b_padded)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6, 7]])
# A + B  # ValueError

def pad_matrix(mat, target_shape, pad_value=0):
    padded = np.full(target_shape, pad_value)
    padded[:mat.shape[0], :mat.shape[1]] = mat
    return padded

A_fixed = pad_matrix(A, (2, 3))
B_fixed = pad_matrix(B, (2, 3))
print(A_fixed + B_fixed)