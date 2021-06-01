# Challenge 1
# Write a NumPy program to compute the mean, standard deviation,



import numpy as np

num = np.arange(1, 21)

mean = np.mean(num)

deviation = np.std(num)

variance = np.var(num)

print("numbers:" + str(num) + "\n" +
      "Mean: " + str(mean) + "\n" +
      "Standard Deviation: " + str(deviation) + "\n" +
      "variance: " + str(variance))

# Challenge 2
# Write a NumPy program to compute the histogram of nums against the bins.

import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.xlabel(' NUMS ')

plt.ylabel('BINS')

plt.title('nums against bins')

plt.hist(nums, bins, color='red')

plt.show()
