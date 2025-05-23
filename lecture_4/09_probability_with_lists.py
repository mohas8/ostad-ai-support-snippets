# Using list to count outcomes (very beginner-friendly)

data = ['H', 'T', 'H', 'H', 'T', 'T', 'H']
prob_H = data.count('H') / len(data)
prob_T = data.count('T') / len(data)

print("P(H):", prob_H)
print("P(T):", prob_T)
