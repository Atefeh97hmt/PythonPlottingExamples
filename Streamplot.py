import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
U = -1 - X**2 + Y
V = 1 + X - Y**2

plt.streamplot(X, Y, U, V, density=1, linewidth=1, arrowsize=1, arrowstyle='->', cmap='viridis')
plt.title('Streamplot')
plt.show()
