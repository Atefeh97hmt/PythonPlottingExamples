import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
r = 1 - np.sin(theta)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rlabel_position(45)
ax.grid(True)

plt.title('Smith Chart')
plt.show()
