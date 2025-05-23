import matplotlib.pyplot as plt

x=7
y=3

# Create the plot
plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')

# Draw x and y axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')


# Set axis limits
plt.xlim(-1, 10)
plt.ylim(-1, 5)
#
# Labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('OStad: 7î + 3ĵ')

# Grid and show
plt.grid()
# plt.gca().set_aspect('auto')
plt.show()