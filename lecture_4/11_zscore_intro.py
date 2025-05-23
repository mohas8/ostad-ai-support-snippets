import statistics

data = [10, 12, 14, 16, 18]
x = 16

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
z_score = (x - mean) / std_dev

print("Z-score of", x, ":", z_score)
