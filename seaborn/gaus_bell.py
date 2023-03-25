#This code generates 1000 random data points from a normal distribution with a mean of 0 and a standard deviation of 0.1,
# creates a histogram of the data, and then plots the bell curve function over the histogram. 
# You can adjust the mean and standard deviation to create different curves.

import numpy as np
import matplotlib.pyplot as plt

# Define the mean and standard deviation of the bell curve
mu, sigma = 0, 0.1

# Generate 1000 random data points from a normal distribution
# with the defined mean and standard deviation
data = np.random.normal(loc=mu, scale=sigma, size=1000)

# Create a histogram of the data
count, bins, ignored = plt.hist(data, 30, density=True)

# Create the bell curve function
bell_curve = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2))

# Plot the bell curve function over the histogram
plt.plot(bins, bell_curve, linewidth=2, color='r')

# Show the plot
plt.show()





