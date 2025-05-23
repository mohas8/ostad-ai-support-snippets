import numpy as np
import matplotlib.pyplot as plt

# Generate data from normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
