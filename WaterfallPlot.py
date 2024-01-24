import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([1, -2, 3, -4, 5])

plt.bar(x, y, align='center')
plt.step(x, np.cumsum(y), where='mid', color='red', linestyle='--')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Waterfall Plot')
plt.show()
