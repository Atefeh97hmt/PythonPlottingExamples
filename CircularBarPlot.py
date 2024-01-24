import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [4, 7, 2, 5, 8]

theta = np.linspace(0.0, 2 * np.pi, len(categories), endpoint=False)

# Repeat the first element to close the circular bar plot
theta = np.concatenate((theta, [theta[0]]))

# Ensure values have the same length as theta
values = np.concatenate((values, [values[0]]))

ax = plt.subplot(111, polar=True)
ax.fill(theta, values, color='skyblue', alpha=0.7)

plt.title('Circular Bar Plot')
plt.show()
