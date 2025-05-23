import matplotlib.pyplot as plt

# Student scores
scores = [88, 38, 45, 55, 65, 78, 92, 12, 37, 80, 82, 45, 89, 32]

# Set pass mark
pass_mark = 50

# Count passed and failed students
passed = sum(score >= pass_mark for score in scores)
failed = len(scores) - passed

# Labels and values
labels = ['Passed', 'Failed']
counts = [passed, failed]
colors = ['green', 'red']

# Plot as a bar chart
plt.figure(figsize=(6, 6))
plt.bar(labels, counts, color=colors)
plt.title('Pass vs Fail Distribution')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='solid', alpha=0.7)
plt.tight_layout()
plt.show()