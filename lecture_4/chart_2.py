import matplotlib.pyplot as plt

scores = [40, 50, 3, 45, 40, 50, 60, 60, 70, 50]

# Create the histogram and get bar containers
counts, bins, patches = plt.hist(scores, bins=10, edgecolor='black')

# Define a list of colors
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'brown', 'gray', 'pink']

# Apply colors to each bar
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

# Add labels and title
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

# Show the plot
plt.tight_layout()
plt.show()