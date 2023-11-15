import matplotlib.pyplot as plt

def plot_lines(x, y, title="Line Plot", xlabel="X-axis", ylabel="Y-axis"):
    plt.plot(x, y, label="Line Plot")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 7, 5]

# Plotting the lines
plot_lines(x_data, y_data)
