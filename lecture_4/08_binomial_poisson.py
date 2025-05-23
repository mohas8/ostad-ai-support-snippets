from scipy.stats import binom, poisson
import matplotlib.pyplot as plt

# Binomial: fixed number of trials, success/failure
n, p = 10, 0.5  # 10 coin tosses, 0.5 chance of heads
x = range(0, 11)
binomial_probs = binom.pmf(x, n, p)

plt.bar(x, binomial_probs)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Successes")
plt.ylabel("Probability")
plt.show()

# Poisson: events in fixed interval
lambda_ = 3
x = range(0, 10)
poisson_probs = poisson.pmf(x, mu=lambda_)

plt.bar(x, poisson_probs, color='orange')
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("Events")
plt.ylabel("Probability")
plt.show()
