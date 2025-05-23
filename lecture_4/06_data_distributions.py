import matplotlib.pyplot as plt

# Simulated data distribution
data = [12, 14, 15, 14, 16, 17, 15, 14, 15, 15, 16, 15]

plt.hist(data, bins=5, edgecolor='black')
plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
