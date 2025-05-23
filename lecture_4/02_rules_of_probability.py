# Basic rules:
# Rule 1: 0 <= P(Event) <= 1
# Rule 2: P(A or B) = P(A) + P(B) - P(A and B)
# Rule 3: P(A and B) = P(A) * P(B), if independent

# Tossing a fair coin
P_heads = 0.5
P_tails = 0.5

# Independent events: Toss 2 coins
P_both_heads = P_heads * P_heads
print("P(both coins are heads):", P_both_heads)
