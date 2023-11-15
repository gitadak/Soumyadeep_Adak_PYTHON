import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency"):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Example data
data = np.random.randn(1000)  # Generating random data for the histogram

# Plotting the histogram
plot_histogram(data)
