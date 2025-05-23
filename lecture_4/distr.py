import matplotlib.pyplot as plt

random_numbers = [1, 10, 11, 12, 21, 34, 31, 33, 40, 45, 100, 101, 201, 25]
plt.hist(random_numbers, bins=5)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()