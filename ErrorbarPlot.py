import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)
y_err = 0.2 * np.abs(np.random.randn(10))  # Ensure non-negative error values

plt.errorbar(x, y, yerr=y_err, fmt='o', color='green', ecolor='red', capsize=3)
plt.title('Errorbar Plot')
plt.show()
