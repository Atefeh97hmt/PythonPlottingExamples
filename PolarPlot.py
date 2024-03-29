import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.sin(6 * theta)

plt.polar(theta, r)
plt.title('Polar Plot')
plt.show()
