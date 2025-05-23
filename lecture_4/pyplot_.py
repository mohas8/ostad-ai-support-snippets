import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data
data = [10, 11, 12, 14, 15, 31, 34, 31, 33]

# Step 2: Calculate variance
variance = np.var(data)  # For population variance
# Use np.var(data, ddof=1) for sample variance

# Step 3: Print variance
print(f"Variance: {variance:.2f}")

# Step 4: Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o', label='Data Points')
plt.axhline(y=np.mean(data), color='red', linestyle='--', label='Mean')
plt.title(f'Data Plot with Variance {variance:.2f}')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()