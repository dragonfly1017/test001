import numpy as np

samples = np.random.normal(-100, 50, 10000)

mean_value = np.mean(samples)
std_deviation = np.std(samples)

print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)
