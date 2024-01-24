import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']
values = [4, 7, 2]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')
plt.show()
