import statistics

data = [5, 10, 15, 20, 25]

# Variance: average of squared differences from the mean
variance = statistics.variance(data)

# Standard deviation: square root of variance
std_dev = statistics.stdev(data)

print("Variance:", variance)
print("Standard Deviation:", std_dev)
