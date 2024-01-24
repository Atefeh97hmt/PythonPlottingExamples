import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', 'Category C']
sizes = [45, 30, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title('Simple Pie Chart')
plt.show()
