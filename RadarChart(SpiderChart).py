import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [4, 7, 2, 5, 8]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

plt.polar(angles, values, marker='o', linestyle='-', color='b')
plt.fill(angles, values, color='b', alpha=0.25)
plt.title('Radar Chart')
plt.show()
