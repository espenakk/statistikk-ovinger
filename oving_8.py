import statistics as st
import numpy as np
from scipy.stats import norm

numbers = [67.52, 69.09, 68.41, 62.73, 63.64]

numbers = [16.49, 16.49, 16.02, 15.86, 16.41,15.86]

print(st.mean(numbers))

new_numbers = []
for i in numbers:
    new_numbers.append(i - 16)

new_numbers_exp = [1.63231622, 1.63231622, 1.02020134, 0.86935824, 1.50681779, 0.86935824]
new_numbers_divided = [0.32646324, 0.32646324, 0.20404027, 0.17387165, 0.30136356, 0.17387165]

yeet = 1.5060736099999998 / 6

print(np.sqrt(yeet))

# Data
measurements = [16.49, 16.49, 16.02, 15.86, 16.41, 15.86]

# Calculate mean
mean = np.mean(measurements)

# Calculate standard deviation
std_dev = np.std(measurements, ddof=1)  # ddof=1 for sample standard deviation

# Calculate t-statistic
t_statistic = (mean - 16) / (std_dev / np.sqrt(len(measurements)))

print("T-statistic:", t_statistic)


# Definer parametrene
mean = 330
std_dev = 2.5 / np.sqrt(5)
critical_value = 327.5

# Beregn z-verdien
z_score = (critical_value - mean) / std_dev

# Beregn sannsynligheten for å få en verdi større enn den kritiske verdien
p_value = 1 - norm.cdf(z_score)

print("Sannsynligheten for en type-1 feil er:", p_value)