import matplotlib.pyplot as plt

def plot_scatter(x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    plt.scatter(x, y, label="Scattered Points")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 7, 5]

# Plotting the scattered points
plot_scatter(x_data, y_data)