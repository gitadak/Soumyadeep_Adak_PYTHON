import matplotlib.pyplot as plt

def plot_pie_chart(labels, sizes, title="Pie Chart"):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    plt.show()

# Example data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 30, 15, 30]

# Plotting the pie chart
plot_pie_chart(labels, sizes)
