from scipy.stats import binom

# Oppgave 4
n = 8
p = 0.82

probability = 1 - binom.cdf(5, n, p)

print(f"The probability of having 6 or more defect-free works out of {n} cars is: {probability:.4f}")